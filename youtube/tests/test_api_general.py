"""
API integration tests for pagination functionality.

These tests focus on API pagination behavior and ensure proper
paginated responses across different endpoints.
"""

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import Video, Comment


class APIPaginationTest(APITestCase):
    """Test suite for API pagination behavior."""

    def setUp(self):
        """Set up test data with multiple videos and comments."""
        self.client = APIClient()

        # Create 25 videos to test pagination (exceeds page size of 20)
        self.videos = []
        for i in range(25):
            video = Video.objects.create(
                title=f"Video {i + 1}", url=f"https://youtube.com/watch?v=test{i + 1}"
            )
            self.videos.append(video)

            # Create 2 comments for each video
            for j in range(2):
                Comment.objects.create(
                    video=video,
                    author=f"Author {i + 1}-{j + 1}",
                    content=f"Comment {j + 1} for Video {i + 1}",
                )

    def test_video_list_pagination_default_page_size(self):
        """Test video list uses default pagination with 20 items per page"""
        url = reverse("video-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertIn("count", response.data)
        self.assertIn("next", response.data)

        # Default page size should be 20
        self.assertEqual(len(response.data["results"]), 20)
        self.assertEqual(response.data["count"], 25)
        self.assertIsNotNone(response.data["next"])

    def test_video_list_pagination_second_page_has_remaining_items(self):
        """Test video list pagination second page has remaining items"""
        url = reverse("video-list")
        response = self.client.get(url, {"page": 2})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 5)  # Remaining items
        self.assertIsNone(response.data["next"])
        self.assertIsNotNone(response.data["previous"])

    def test_comment_list_filtered_by_video_respects_pagination(self):
        """Test comment filtering by video works with pagination"""
        test_video = self.videos[0]

        # Add more comments to test pagination
        for i in range(18):  # Plus 2 existing = 20 comments (full page)
            Comment.objects.create(
                video=test_video,
                author=f"Extra Author {i}",
                content=f"Extra Comment {i}",
            )

        url = reverse("comment-list")
        response = self.client.get(url, {"video": test_video.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 20)  # Full page
        self.assertEqual(response.data["count"], 20)  # 2 original + 18 new

        # All comments should be for the specified video
        for comment in response.data["results"]:
            self.assertEqual(comment["video"], test_video.id)

    def test_pagination_invalid_page_returns_404(self):
        """Test invalid page number returns 404 error"""
        url = reverse("video-list")
        response = self.client.get(url, {"page": 999})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_pagination_non_numeric_page_returns_404(self):
        """Test non-numeric page parameter returns 404 error"""
        url = reverse("video-list")
        response = self.client.get(url, {"page": "invalid"})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class APIErrorHandlingTest(APITestCase):
    """Test suite for API error handling."""

    def setUp(self):
        """Set up test client for error handling tests."""
        self.client = APIClient()

    def test_invalid_video_id_format_returns_404(self):
        """Test API response for invalid ID format returns 404"""
        url = "/api/videos/invalid-id/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed_on_action_endpoints(self):
        """Test method not allowed responses for custom action endpoints"""
        # Create a video first
        video = Video.objects.create(
            title="Test Video", url="https://youtube.com/watch?v=test"
        )

        # GET not allowed on increment_views (only POST)
        url = reverse("video-increment-views", args=[video.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # GET not allowed on like (only POST)
        url = reverse("video-like", args=[video.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_empty_request_body_returns_validation_errors(self):
        """Test empty POST request returns field validation errors"""
        url = reverse("video-list")
        response = self.client.post(url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertIn("url", response.data)

    def test_malformed_json_returns_400(self):
        """Test malformed JSON returns 400 error"""
        url = reverse("video-list")
        response = self.client.post(
            url, '{"title": "Test", invalid json}', content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

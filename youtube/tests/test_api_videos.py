"""
Integration tests for Video API endpoints.

These tests focus on HTTP requests/responses, API behavior, serialization,
and integration between different components.
"""

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import Video, Comment


class VideoAPITest(APITestCase):
    """Test suite for Video API endpoints functionality."""

    def setUp(self):
        """Set up test data and client for each test method."""
        self.client = APIClient()
        self.video = self._create_video(
            title="Test Video",
            description="A test video",
            url="https://youtube.com/watch?v=test123",
            thumbnail_url="https://img.youtube.com/vi/test123/maxresdefault.jpg",
            duration=300,
            view_count=100,
            like_count=10,
        )

    def _create_video(self, **kwargs):
        """Helper method to create video instances with default values."""
        defaults = {
            "title": "Default Video",
            "url": "https://youtube.com/watch?v=default",
        }
        defaults.update(kwargs)
        return Video.objects.create(**defaults)

    def test_get_video_list(self):
        """Test GET /api/videos/ - List all videos"""
        url = reverse("video-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Test Video")
        self.assertIn("comments_count", response.data["results"][0])

    def test_get_video_detail(self):
        """Test GET /api/videos/{id}/ - Get video details with comments"""
        url = reverse("video-detail", args=[self.video.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Video")
        self.assertEqual(response.data["description"], "A test video")
        self.assertEqual(response.data["url"], "https://youtube.com/watch?v=test123")
        self.assertEqual(response.data["duration"], 300)
        self.assertEqual(response.data["view_count"], 100)
        self.assertEqual(response.data["like_count"], 10)
        self.assertIn("comments", response.data)

    def test_get_video_detail_with_comments(self):
        """Test GET /api/videos/{id}/ - Get video details with associated comments"""
        # Create some comments for the video
        Comment.objects.create(
            video=self.video, author="Author 1", content="First comment"
        )
        Comment.objects.create(
            video=self.video, author="Author 2", content="Second comment"
        )

        url = reverse("video-detail", args=[self.video.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("comments", response.data)
        self.assertEqual(len(response.data["comments"]), 2)

        # Check comment structure
        comment = response.data["comments"][0]
        self.assertIn("id", comment)
        self.assertIn("author", comment)
        self.assertIn("content", comment)
        self.assertIn("like_count", comment)
        self.assertIn("created_at", comment)

    def test_create_video(self):
        """Test POST /api/videos/ - Create a new video"""
        url = reverse("video-list")
        data = {
            "title": "New Test Video",
            "description": "A new test video",
            "url": "https://youtube.com/watch?v=new123",
            "thumbnail_url": "https://img.youtube.com/vi/new123/maxresdefault.jpg",
            "duration": 240,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 2)
        new_video = Video.objects.get(url="https://youtube.com/watch?v=new123")
        self.assertEqual(new_video.title, "New Test Video")
        self.assertEqual(new_video.duration, 240)

    def test_create_video_with_invalid_data_returns_validation_errors(self):
        """Test POST with invalid data returns 400 with field errors"""
        url = reverse("video-list")
        data = {
            "title": "",  # Required field
            "url": "invalid-url",  # Invalid URL format
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_create_video_with_duplicate_url_returns_validation_error(self):
        """Test POST with duplicate URL returns 400"""
        url = reverse("video-list")
        data = {
            "title": "Duplicate Video",
            "url": self.video.url,  # Same URL as existing video
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_update_video_updates_specified_fields_only(self):
        """Test PATCH updates only specified fields"""
        url = reverse("video-detail", args=[self.video.id])
        original_description = self.video.description
        data = {"title": "Updated Title Only"}

        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.video.refresh_from_db()
        self.assertEqual(self.video.title, "Updated Title Only")
        self.assertEqual(self.video.description, original_description)  # Unchanged

    def test_delete_video_cascades_to_comments(self):
        """Test DELETE video removes associated comments via CASCADE"""
        # Create comments
        Comment.objects.create(video=self.video, author="Author 1", content="Comment 1")
        Comment.objects.create(video=self.video, author="Author 2", content="Comment 2")

        self.assertEqual(Comment.objects.count(), 2)

        url = reverse("video-detail", args=[self.video.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Video.objects.count(), 0)
        self.assertEqual(Comment.objects.count(), 0)  # Cascade deletion

    def test_increment_views(self):
        """Test POST /api/videos/{id}/increment_views/ - Increment view count"""
        url = reverse("video-increment-views", args=[self.video.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["view_count"], 101)
        self.video.refresh_from_db()
        self.assertEqual(self.video.view_count, 101)

    def test_like_video_returns_updated_count(self):
        """Test POST /api/videos/{id}/like/ increments and returns new count"""
        url = reverse("video-like", args=[self.video.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["like_count"], 11)
        self.video.refresh_from_db()
        self.assertEqual(self.video.like_count, 11)

    def test_video_not_found(self):
        """Test getting non-existent video"""
        url = reverse("video-detail", args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_increment_views_nonexistent_video(self):
        """Test incrementing views for non-existent video"""
        url = reverse("video-increment-views", args=[999])
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_like_nonexistent_video(self):
        """Test liking non-existent video"""
        url = reverse("video-like", args=[999])
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_video_list_includes_pagination_and_comments_count(self):
        """Test video list API includes pagination and nested comments count"""
        url = reverse("video-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertIn("count", response.data)

        # Verify comments_count is included in list view
        if response.data["results"]:
            video = response.data["results"][0]
            self.assertIn("comments_count", video)

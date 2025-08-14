"""
Integration tests for Comment API endpoints.

These tests focus on HTTP requests/responses, API behavior, serialization,
and integration between different components.
"""

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import Video, Comment


class CommentAPITest(APITestCase):
    """Test suite for Comment API endpoints functionality."""

    def setUp(self):
        """Set up test data and client for each test method."""
        self.client = APIClient()
        self.video1 = self._create_video(
            title="Test Video 1", url="https://youtube.com/watch?v=test123"
        )
        self.video2 = self._create_video(
            title="Test Video 2", url="https://youtube.com/watch?v=test456"
        )
        self.comment1 = self._create_comment(
            video=self.video1, author="Author 1", content="First comment", like_count=5
        )
        self.comment2 = self._create_comment(
            video=self.video2, author="Author 2", content="Second comment", like_count=3
        )

    def _create_video(self, **kwargs):
        """Helper method to create video instances."""
        defaults = {
            "title": "Default Video",
            "url": "https://youtube.com/watch?v=default",
        }
        defaults.update(kwargs)
        return Video.objects.create(**defaults)

    def _create_comment(self, **kwargs):
        """Helper method to create comment instances."""
        defaults = {"author": "Default Author", "content": "Default comment content"}
        defaults.update(kwargs)
        return Comment.objects.create(**defaults)

    def test_get_comment_list(self):
        """Test GET /api/comments/ - List all comments"""
        url = reverse("comment-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertEqual(len(response.data["results"]), 2)

    def test_get_comment_list_filtered_by_video(self):
        """Test GET /api/comments/?video=1 - List comments for specific video"""
        url = reverse("comment-list")
        response = self.client.get(url, {"video": self.video1.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["author"], "Author 1")

    def test_get_comment_list_filtered_by_nonexistent_video(self):
        """Test filtering comments by non-existent video returns empty results"""
        url = reverse("comment-list")
        response = self.client.get(url, {"video": 999})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 0)

    def test_get_comment_detail(self):
        """Test GET /api/comments/{id}/ - Get comment details"""
        url = reverse("comment-detail", args=[self.comment1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["author"], "Author 1")
        self.assertEqual(response.data["content"], "First comment")
        self.assertEqual(response.data["like_count"], 5)

    def test_create_comment(self):
        """Test POST /api/comments/ - Create a new comment"""
        url = reverse("comment-list")
        data = {
            "video": self.video1.id,
            "author": "New Author",
            "content": "This is a new comment",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 3)
        new_comment = Comment.objects.get(author="New Author")
        self.assertEqual(new_comment.content, "This is a new comment")
        self.assertEqual(new_comment.video, self.video1)

    def test_create_comment_with_invalid_video_returns_validation_error(self):
        """Test POST with non-existent video returns 400"""
        url = reverse("comment-list")
        data = {
            "video": 999,  # Non-existent video
            "author": "Author",
            "content": "Comment",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_create_comment_with_missing_required_fields_returns_validation_errors(
        self,
    ):
        """Test POST with missing required fields returns 400 with field errors"""
        url = reverse("comment-list")
        data = {
            "video": self.video1.id,
            "author": "",  # Required field
            "content": "",  # Required field
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_update_comment_updates_specified_fields_only(self):
        """Test PATCH updates only specified fields"""
        url = reverse("comment-detail", args=[self.comment1.id])
        original_author = self.comment1.author
        data = {"content": "Updated content only"}

        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.content, "Updated content only")
        self.assertEqual(self.comment1.author, original_author)  # Unchanged

    def test_like_comment_returns_updated_count(self):
        """Test POST /api/comments/{id}/like/ increments and returns new count"""
        url = reverse("comment-like", args=[self.comment1.id])
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["like_count"], 6)
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.like_count, 6)

    def test_comment_not_found(self):
        """Test getting non-existent comment"""
        url = reverse("comment-detail", args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_like_nonexistent_comment(self):
        """Test liking non-existent comment"""
        url = reverse("comment-like", args=[999])
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

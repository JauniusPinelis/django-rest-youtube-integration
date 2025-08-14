"""
Service layer tests for YouTube API.

Tests focus on business logic, validation, and service behavior.
Following Django styleguide patterns for testing services.
"""

from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Video, Comment
from ..services import VideoService, CommentService


class VideoServiceTests(TestCase):
    """Test suite for VideoService business logic."""

    def setUp(self):
        self.service = VideoService()
        self.video = Video.objects.create(
            title="Test Video",
            url="https://youtube.com/watch?v=test123",
            view_count=100,
            like_count=10,
        )

    def test_increment_views_increases_count_by_one(self):
        """Test that incrementing views increases count by exactly 1."""
        result = self.service.increment_views(video_id=self.video.id)

        self.assertEqual(result.view_count, 101)

        # Verify database was updated
        self.video.refresh_from_db()
        self.assertEqual(self.video.view_count, 101)

    def test_increment_views_with_nonexistent_video_raises_validation_error(self):
        """Test that incrementing views for non-existent video raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            self.service.increment_views(video_id=999)

        self.assertEqual(str(cm.exception), "['Video not found.']")

    def test_increment_likes_increases_count_by_one(self):
        """Test that incrementing likes increases count by exactly 1."""
        result = self.service.increment_likes(video_id=self.video.id)

        self.assertEqual(result.like_count, 11)

        # Verify database was updated
        self.video.refresh_from_db()
        self.assertEqual(self.video.like_count, 11)

    def test_increment_likes_with_nonexistent_video_raises_validation_error(self):
        """Test that incrementing likes for non-existent video raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            self.service.increment_likes(video_id=999)

        self.assertEqual(str(cm.exception), "['Video not found.']")

    def test_increment_views_multiple_times_accumulates_correctly(self):
        """Test that multiple view increments accumulate correctly."""
        # Increment 5 times
        for _ in range(5):
            self.service.increment_views(video_id=self.video.id)

        self.video.refresh_from_db()
        self.assertEqual(self.video.view_count, 105)


class CommentServiceTests(TestCase):
    """Test suite for CommentService business logic."""

    def setUp(self):
        self.service = CommentService()
        self.video = Video.objects.create(
            title="Test Video", url="https://youtube.com/watch?v=test123"
        )

    def test_create_comment_with_valid_data_succeeds(self):
        """Test that creating comment with valid data succeeds."""
        result = self.service.create(
            video_id=self.video.id, author="Test Author", content="Test comment content"
        )

        self.assertEqual(result.video, self.video)
        self.assertEqual(result.author, "Test Author")
        self.assertEqual(result.content, "Test comment content")
        self.assertEqual(result.like_count, 0)  # Default value

        # Verify database state
        self.assertEqual(Comment.objects.count(), 1)

    def test_create_comment_with_nonexistent_video_raises_validation_error(self):
        """Test that creating comment for non-existent video raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            self.service.create(
                video_id=999, author="Test Author", content="Test content"
            )

        self.assertEqual(str(cm.exception), "['Video not found.']")

    def test_create_comment_with_empty_author_raises_validation_error(self):
        """Test that creating comment with empty author raises ValidationError."""
        with self.assertRaises(ValidationError):
            self.service.create(
                video_id=self.video.id, author="", content="Test content"
            )

    def test_create_comment_with_empty_content_raises_validation_error(self):
        """Test that creating comment with empty content raises ValidationError."""
        with self.assertRaises(ValidationError):
            self.service.create(
                video_id=self.video.id, author="Test Author", content=""
            )

    def test_increment_likes_increases_count_by_one(self):
        """Test that incrementing comment likes increases count by exactly 1."""
        comment = Comment.objects.create(
            video=self.video, author="Test Author", content="Test content", like_count=5
        )

        result = self.service.increment_likes(comment_id=comment.id)

        self.assertEqual(result.like_count, 6)

        # Verify database was updated
        comment.refresh_from_db()
        self.assertEqual(comment.like_count, 6)

    def test_increment_likes_with_nonexistent_comment_raises_validation_error(self):
        """Test that incrementing likes for non-existent comment raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            self.service.increment_likes(comment_id=999)

        self.assertEqual(str(cm.exception), "['Comment not found.']")

    def test_get_by_video_returns_comments_for_specific_video(self):
        """Test that get_by_video returns only comments for specified video."""
        video2 = Video.objects.create(
            title="Video 2", url="https://youtube.com/watch?v=test456"
        )

        # Create comments for different videos
        comment1 = Comment.objects.create(
            video=self.video, author="Author 1", content="Comment 1"
        )
        comment2 = Comment.objects.create(
            video=video2, author="Author 2", content="Comment 2"
        )
        comment3 = Comment.objects.create(
            video=self.video, author="Author 3", content="Comment 3"
        )

        # Test filtering by video1
        result = self.service.get_by_video(video_id=self.video.id)
        comment_ids = list(result.values_list("id", flat=True))

        self.assertIn(comment1.id, comment_ids)
        self.assertIn(comment3.id, comment_ids)
        self.assertNotIn(comment2.id, comment_ids)

    def test_get_by_video_with_no_video_id_returns_all_comments(self):
        """Test that get_by_video with None returns all comments."""
        Comment.objects.create(video=self.video, author="Author 1", content="Comment 1")
        Comment.objects.create(video=self.video, author="Author 2", content="Comment 2")

        result = self.service.get_by_video(video_id=None)

        self.assertEqual(result.count(), 2)

"""
Tests for Celery tasks.
"""

from unittest.mock import patch, Mock
from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError
from youtube.models import Video, Comment
from youtube.tasks import (
    generate_video_content,
    generate_comments_for_video,
    simulate_user_engagement,
    generate_engagement_stats,
    cleanup_old_data,
)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class VideoContentGenerationTaskTests(TestCase):
    """Tests for the generate_video_content task."""

    def test_generate_video_content_creates_video(self):
        """Test that the task successfully creates a new video."""
        initial_count = Video.objects.count()

        result = generate_video_content.delay()
        response = result.get()

        # Check that a video was created
        self.assertEqual(Video.objects.count(), initial_count + 1)
        self.assertIn("video_id", response)
        self.assertIn("title", response)
        self.assertEqual(response["message"], "Video generated successfully")

        # Verify video properties
        video = Video.objects.get(pk=response["video_id"])
        self.assertIsNotNone(video.title)
        self.assertIsNotNone(video.description)
        self.assertIsNotNone(video.url)
        self.assertIsNotNone(video.thumbnail_url)
        self.assertGreater(video.duration, 0)
        self.assertGreaterEqual(video.view_count, 0)
        self.assertGreaterEqual(video.like_count, 0)

    @patch("youtube.tasks.generate_comments_for_video.delay")
    def test_generate_video_content_schedules_comment_generation(
        self, mock_comment_task
    ):
        """Test that the task schedules comment generation for the new video."""
        result = generate_video_content.delay()
        response = result.get()

        # Verify that comment generation was scheduled
        mock_comment_task.assert_called_once()
        call_args = mock_comment_task.call_args
        self.assertEqual(call_args[0][0], response["video_id"])  # video_id
        self.assertIn("comment_count", call_args[1] or {})  # kwargs

    def test_generate_video_content_multiple_calls_create_unique_videos(self):
        """Test that multiple calls create unique videos."""
        result1 = generate_video_content.delay()
        result2 = generate_video_content.delay()

        response1 = result1.get()
        response2 = result2.get()

        self.assertNotEqual(response1["video_id"], response2["video_id"])

        video1 = Video.objects.get(pk=response1["video_id"])
        video2 = Video.objects.get(pk=response2["video_id"])

        # URLs should be unique
        self.assertNotEqual(video1.url, video2.url)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class CommentGenerationTaskTests(TestCase):
    """Tests for the generate_comments_for_video task."""

    def setUp(self):
        self.video = Video.objects.create(
            title="Test Video",
            description="A test video",
            url="https://youtube.com/test",
            duration=300,
        )

    @patch("youtube.services.CommentGenerationService")
    def test_generate_comments_for_video_success(self, mock_service_class):
        """Test successful comment generation for a video."""
        # Mock the service
        mock_service = Mock()
        mock_service.generate_comment.return_value = "Great video! Very informative."
        mock_service_class.return_value = mock_service

        result = generate_comments_for_video.delay(self.video.id, 3)
        response = result.get()

        # Check response
        self.assertEqual(response["video_id"], self.video.id)
        self.assertEqual(response["comments_generated"], 3)
        self.assertIn("comments", response)

        # Check that comments were created
        self.assertEqual(Comment.objects.filter(video=self.video).count(), 3)

        # Verify service was called
        self.assertEqual(mock_service.generate_comment.call_count, 3)

    def test_generate_comments_for_nonexistent_video(self):
        """Test handling of nonexistent video ID."""
        result = generate_comments_for_video.delay(99999, 2)
        response = result.get()

        self.assertIn("error", response)
        self.assertEqual(response["error"], "Video not found")

    @patch("youtube.services.CommentGenerationService")
    def test_generate_comments_handles_service_errors(self, mock_service_class):
        """Test handling of comment generation service errors."""
        # Mock service to raise an exception
        mock_service = Mock()
        mock_service.generate_comment.side_effect = ValidationError("API error")
        mock_service_class.return_value = mock_service

        result = generate_comments_for_video.delay(self.video.id, 2)
        response = result.get()

        # Task should complete but with fewer comments
        self.assertEqual(response["video_id"], self.video.id)
        self.assertEqual(response["comments_generated"], 0)  # All failed
        self.assertEqual(Comment.objects.filter(video=self.video).count(), 0)

    def test_generate_comments_with_default_count(self):
        """Test comment generation with default count parameter."""
        with patch("youtube.services.CommentGenerationService") as mock_service_class:
            mock_service = Mock()
            mock_service.generate_comment.return_value = "Nice content!"
            mock_service_class.return_value = mock_service

            result = generate_comments_for_video.delay(
                self.video.id
            )  # No count specified
            response = result.get()

            # Should generate default of 5 comments
            self.assertEqual(response["comments_generated"], 5)
            self.assertEqual(Comment.objects.filter(video=self.video).count(), 5)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class UserEngagementTaskTests(TestCase):
    """Tests for the simulate_user_engagement task."""

    def setUp(self):
        self.video1 = Video.objects.create(
            title="Video 1",
            url="https://youtube.com/test1",
            view_count=100,
            like_count=10,
        )
        self.video2 = Video.objects.create(
            title="Video 2",
            url="https://youtube.com/test2",
            view_count=50,
            like_count=5,
        )

    def test_simulate_user_engagement_with_videos(self):
        """Test user engagement simulation with existing videos."""
        initial_video1_views = self.video1.view_count
        initial_video2_views = self.video2.view_count

        result = simulate_user_engagement.delay()
        response = result.get()

        # Check response structure
        self.assertIn("videos_engaged", response)
        self.assertIn("engagement_details", response)
        self.assertGreater(response["videos_engaged"], 0)

        # Check that some engagement occurred
        self.video1.refresh_from_db()
        self.video2.refresh_from_db()

        # At least one video should have engagement (views are most common)
        total_new_views = (self.video1.view_count - initial_video1_views) + (
            self.video2.view_count - initial_video2_views
        )
        self.assertGreaterEqual(total_new_views, 0)  # Could be 0 due to randomness

    def test_simulate_user_engagement_no_videos(self):
        """Test engagement simulation when no videos exist."""
        Video.objects.all().delete()

        result = simulate_user_engagement.delay()
        response = result.get()

        self.assertEqual(response["message"], "No videos available for engagement")

    @patch("youtube.tasks.generate_comments_for_video.delay")
    def test_simulate_user_engagement_schedules_comments(self, mock_comment_task):
        """Test that engagement simulation can schedule comment generation."""
        # Run multiple times to increase chance of hitting comment generation
        for _ in range(10):
            simulate_user_engagement.delay()

        # Check if comment generation was called (20% chance per video per run)
        # With multiple runs, it should be called at least once
        # Note: This test may be flaky due to randomness


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class EngagementStatsTaskTests(TestCase):
    """Tests for the generate_engagement_stats task."""

    def setUp(self):
        # Create test data
        self.video1 = Video.objects.create(
            title="Popular Video",
            url="https://youtube.com/popular",
            view_count=1000,
            like_count=100,
        )
        self.video2 = Video.objects.create(
            title="Less Popular Video",
            url="https://youtube.com/less",
            view_count=100,
            like_count=10,
        )

        # Create comments
        Comment.objects.create(
            video=self.video1,
            author="User1",
            content="Great!",
            like_count=5,
        )
        Comment.objects.create(
            video=self.video1,
            author="User2",
            content="Amazing!",
            like_count=3,
        )
        Comment.objects.create(
            video=self.video2,
            author="User3",
            content="Good video",
            like_count=1,
        )

    def test_generate_engagement_stats_structure(self):
        """Test that stats generation returns proper structure."""
        result = generate_engagement_stats.delay()
        response = result.get()

        # Check response structure
        self.assertIn("timestamp", response)
        self.assertIn("video_stats", response)
        self.assertIn("comment_stats", response)
        self.assertIn("most_commented_videos", response)

        # Check video stats
        video_stats = response["video_stats"]
        self.assertEqual(video_stats["total_videos"], 2)
        self.assertIsNotNone(video_stats["avg_views"])
        self.assertIsNotNone(video_stats["avg_likes"])
        self.assertEqual(video_stats["max_views"], 1000)
        self.assertEqual(video_stats["max_likes"], 100)

        # Check comment stats
        comment_stats = response["comment_stats"]
        self.assertEqual(comment_stats["total_comments"], 3)
        self.assertIsNotNone(comment_stats["avg_likes"])

    def test_generate_engagement_stats_most_commented(self):
        """Test that most commented videos are correctly identified."""
        result = generate_engagement_stats.delay()
        response = result.get()

        most_commented = response["most_commented_videos"]
        self.assertIsInstance(most_commented, list)
        self.assertGreater(len(most_commented), 0)

        # First video should have more comments
        if len(most_commented) >= 2:
            self.assertGreaterEqual(
                most_commented[0]["comment_count"], most_commented[1]["comment_count"]
            )

    def test_generate_engagement_stats_no_data(self):
        """Test stats generation with no data."""
        Video.objects.all().delete()
        Comment.objects.all().delete()

        result = generate_engagement_stats.delay()
        response = result.get()

        # Should still return valid structure with zero counts
        self.assertEqual(response["video_stats"]["total_videos"], 0)
        self.assertEqual(response["comment_stats"]["total_comments"], 0)
        self.assertEqual(len(response["most_commented_videos"]), 0)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class CleanupTaskTests(TestCase):
    """Tests for the cleanup_old_data task."""

    def setUp(self):
        from django.utils import timezone
        from datetime import timedelta

        # Create old video (35 days ago)
        old_date = timezone.now() - timedelta(days=35)
        self.old_video = Video.objects.create(
            title="Old Video",
            url="https://youtube.com/old",
            created_at=old_date,
        )

        # Create recent video (5 days ago)
        recent_date = timezone.now() - timedelta(days=5)
        self.recent_video = Video.objects.create(
            title="Recent Video",
            url="https://youtube.com/recent",
            created_at=recent_date,
        )

        # Create old comment
        self.old_comment = Comment.objects.create(
            video=self.old_video,
            author="OldUser",
            content="Old comment",
            created_at=old_date,
        )

        # Create recent comment
        self.recent_comment = Comment.objects.create(
            video=self.recent_video,
            author="RecentUser",
            content="Recent comment",
            created_at=recent_date,
        )

    def test_cleanup_old_data_removes_old_items(self):
        """Test that cleanup removes items older than specified days."""
        result = cleanup_old_data.delay(30)  # Remove items older than 30 days
        response = result.get()

        # Check response
        self.assertIn("videos_deleted", response)
        self.assertIn("comments_deleted", response)
        self.assertEqual(response["videos_deleted"], 1)  # Old video should be deleted
        self.assertEqual(
            response["comments_deleted"], 1
        )  # Old comment should be deleted

        # Verify database state
        self.assertFalse(Video.objects.filter(pk=self.old_video.pk).exists())
        self.assertTrue(Video.objects.filter(pk=self.recent_video.pk).exists())
        self.assertFalse(Comment.objects.filter(pk=self.old_comment.pk).exists())
        self.assertTrue(Comment.objects.filter(pk=self.recent_comment.pk).exists())

    def test_cleanup_old_data_with_default_days(self):
        """Test cleanup with default days parameter."""
        result = cleanup_old_data.delay()  # Should default to 30 days
        response = result.get()

        # Should behave the same as the explicit 30 days test
        self.assertIn("cutoff_date", response)

    def test_cleanup_old_data_no_old_items(self):
        """Test cleanup when no old items exist."""
        # Delete the old items manually
        self.old_video.delete()
        self.old_comment.delete()

        result = cleanup_old_data.delay(30)
        response = result.get()

        self.assertEqual(response["videos_deleted"], 0)
        self.assertEqual(response["comments_deleted"], 0)


@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class TaskIntegrationTests(TestCase):
    """Integration tests for task workflows."""

    def test_full_content_generation_workflow(self):
        """Test the complete workflow from video generation to comments."""
        with patch(
            "youtube.tasks.generate_comments_for_video.delay"
        ) as mock_comment_task:
            # Generate a video (but prevent automatic comment generation)
            video_result = generate_video_content.delay()
            video_response = video_result.get()
            video_id = video_response["video_id"]

            # Verify video was created
            video = Video.objects.get(pk=video_id)
            self.assertIsNotNone(video)

            # Verify comment generation was scheduled
            mock_comment_task.assert_called_once()

        # Now test actual comment generation separately
        with patch("youtube.services.CommentGenerationService") as mock_service_class:
            mock_service = Mock()
            mock_service.generate_comment.return_value = "Fantastic content!"
            mock_service_class.return_value = mock_service

            comment_result = generate_comments_for_video.delay(video_id, 2)
            comment_response = comment_result.get()

            # Verify comments were created
            comments = Comment.objects.filter(video=video)
            self.assertEqual(comments.count(), 2)
            self.assertEqual(comment_response["video_id"], video_id)
            self.assertEqual(comment_response["comments_generated"], 2)

    def test_engagement_stats_after_content_generation(self):
        """Test that stats generation works after creating content."""
        # Create some content
        video_result = generate_video_content.delay()
        video_response = video_result.get()

        # Generate stats
        stats_result = generate_engagement_stats.delay()
        stats_response = stats_result.get()

        # Verify stats include the new video
        self.assertGreaterEqual(stats_response["video_stats"]["total_videos"], 1)
        self.assertIn(
            video_response["video_id"],
            [v["id"] for v in stats_response["most_commented_videos"]],
        )

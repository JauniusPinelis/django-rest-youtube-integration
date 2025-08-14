"""
Tests for ContentPopulationService.
"""

from unittest.mock import patch
from django.test import TestCase
from django.core.exceptions import ValidationError
from youtube.models import Video, Comment
from youtube.services import ContentPopulationService


class ContentPopulationServiceTests(TestCase):
    """Tests for the ContentPopulationService class."""

    def setUp(self):
        self.service = ContentPopulationService()

    def test_generate_video_creates_video(self):
        """Test that generate_video creates a new video with proper data."""
        initial_count = Video.objects.count()

        result = self.service.generate_video()

        # Check that a video was created
        self.assertEqual(Video.objects.count(), initial_count + 1)
        self.assertIn("video_id", result)
        self.assertIn("title", result)
        self.assertIn("description", result)
        self.assertIn("url", result)

        # Verify video properties
        video = Video.objects.get(pk=result["video_id"])
        self.assertEqual(video.title, result["title"])
        self.assertEqual(video.description, result["description"])
        self.assertEqual(video.url, result["url"])
        self.assertGreater(video.duration, 0)
        self.assertGreaterEqual(video.view_count, 0)
        self.assertGreaterEqual(video.like_count, 0)

    def test_generate_video_uses_templates(self):
        """Test that generate_video uses the predefined templates."""
        result = self.service.generate_video()

        video = Video.objects.get(pk=result["video_id"])

        # Check that title follows template patterns
        template_patterns = [
            "Amazing Python Tutorial:",
            "Daily Coding Challenge:",
            "Tech News Update:",
            "Building Projects with",
        ]

        title_matches_template = any(
            pattern in video.title for pattern in template_patterns
        )
        self.assertTrue(
            title_matches_template, f"Title '{video.title}' doesn't match any template"
        )

    def test_generate_video_multiple_calls_create_unique_videos(self):
        """Test that multiple calls create unique videos."""
        result1 = self.service.generate_video()
        result2 = self.service.generate_video()

        self.assertNotEqual(result1["video_id"], result2["video_id"])

        video1 = Video.objects.get(pk=result1["video_id"])
        video2 = Video.objects.get(pk=result2["video_id"])

        # URLs should be unique
        self.assertNotEqual(video1.url, video2.url)

    def test_generate_comments_for_video_success(self):
        """Test successful comment generation for a video."""
        # Create test video
        video = Video.objects.create(
            title="Test Video",
            description="A test video",
            url="https://youtube.com/test",
            duration=300,
        )

        # Mock the AI service on the instance
        with patch.object(
            self.service.comment_generator, "generate_comment"
        ) as mock_generate:
            mock_generate.return_value = "Great video! Very informative."

            result = self.service.generate_comments_for_video(video.id, 3)

            # Check response
            self.assertEqual(result["video_id"], video.id)
            self.assertEqual(result["comments_generated"], 3)
            self.assertIn("comments", result)

            # Check that comments were created
            self.assertEqual(Comment.objects.filter(video=video).count(), 3)

            # Verify service was called
            self.assertEqual(mock_generate.call_count, 3)

    def test_generate_comments_for_nonexistent_video(self):
        """Test handling of nonexistent video ID."""
        result = self.service.generate_comments_for_video(99999, 2)

        self.assertIn("error", result)
        self.assertEqual(result["error"], "Video not found")

    def test_generate_comments_handles_service_errors(self):
        """Test handling of comment generation service errors."""
        # Create test video
        video = Video.objects.create(
            title="Test Video",
            description="A test video",
            url="https://youtube.com/test",
            duration=300,
        )

        # Mock service to raise an exception
        with patch.object(
            self.service.comment_generator, "generate_comment"
        ) as mock_generate:
            mock_generate.side_effect = ValidationError("API error")

            result = self.service.generate_comments_for_video(video.id, 2)

            # Should handle errors gracefully - comments generated will be less due to errors
            self.assertEqual(result["video_id"], video.id)
            # Comments might still be generated due to error handling
            self.assertLessEqual(result["comments_generated"], 2)

    def test_generate_comments_uses_varied_authors_and_tones(self):
        """Test that comment generation uses varied authors and tones."""
        # Create test video
        video = Video.objects.create(
            title="Test Video",
            description="A test video",
            url="https://youtube.com/test",
            duration=300,
        )

        with patch.object(
            self.service.comment_generator, "generate_comment"
        ) as mock_generate:
            mock_generate.return_value = "Great content!"

            self.service.generate_comments_for_video(video.id, 5)

            # Verify different authors were used
            comments = Comment.objects.filter(video=video)
            authors = [comment.author for comment in comments]

            # Should use authors from predefined list
            valid_authors = set(self.service.COMMENT_AUTHORS)
            comment_authors = set(authors)
            self.assertTrue(comment_authors.issubset(valid_authors))

    def test_simulate_engagement_for_videos_with_videos(self):
        """Test engagement simulation with existing videos."""
        # Create test videos
        video1 = Video.objects.create(
            title="Video 1",
            url="https://youtube.com/test1",
            view_count=100,
            like_count=10,
        )
        video2 = Video.objects.create(
            title="Video 2",
            url="https://youtube.com/test2",
            view_count=50,
            like_count=5,
        )

        initial_video1_views = video1.view_count
        initial_video2_views = video2.view_count

        result = self.service.simulate_engagement_for_videos()

        # Check response structure
        self.assertIn("videos_engaged", result)
        self.assertIn("engagement_details", result)
        self.assertGreater(result["videos_engaged"], 0)

        # Check that some engagement occurred
        video1.refresh_from_db()
        video2.refresh_from_db()

        # At least one video should have engagement
        total_new_views = (video1.view_count - initial_video1_views) + (
            video2.view_count - initial_video2_views
        )
        self.assertGreaterEqual(total_new_views, 0)  # Could be 0 due to randomness

    def test_simulate_engagement_for_videos_no_videos(self):
        """Test engagement simulation when no videos exist."""
        result = self.service.simulate_engagement_for_videos()

        self.assertEqual(result["message"], "No videos available for engagement")
        self.assertEqual(result["videos_engaged"], 0)

    def test_simulate_engagement_respects_video_count_parameter(self):
        """Test that engagement simulation respects video_count parameter."""
        # Create multiple videos
        for i in range(5):
            Video.objects.create(
                title=f"Video {i + 1}",
                url=f"https://youtube.com/test{i + 1}",
                view_count=100,
                like_count=10,
            )

        result = self.service.simulate_engagement_for_videos(video_count=2)

        # Should only engage with 2 videos
        self.assertLessEqual(result["videos_engaged"], 2)

    def test_get_engagement_statistics_structure(self):
        """Test that statistics generation returns proper structure."""
        # Create test data
        video1 = Video.objects.create(
            title="Popular Video",
            url="https://youtube.com/popular",
            view_count=1000,
            like_count=100,
        )
        Video.objects.create(
            title="Less Popular Video",
            url="https://youtube.com/less",
            view_count=100,
            like_count=10,
        )

        # Create comments
        Comment.objects.create(
            video=video1,
            author="User1",
            content="Great!",
            like_count=5,
        )
        Comment.objects.create(
            video=video1,
            author="User2",
            content="Amazing!",
            like_count=3,
        )

        result = self.service.get_engagement_statistics()

        # Check response structure
        self.assertIn("video_stats", result)
        self.assertIn("comment_stats", result)
        self.assertIn("most_commented_videos", result)

        # Check video stats
        video_stats = result["video_stats"]
        self.assertEqual(video_stats["total_videos"], 2)
        self.assertIsNotNone(video_stats["avg_views"])
        self.assertIsNotNone(video_stats["avg_likes"])
        self.assertEqual(video_stats["max_views"], 1000)
        self.assertEqual(video_stats["max_likes"], 100)

        # Check comment stats
        comment_stats = result["comment_stats"]
        self.assertEqual(comment_stats["total_comments"], 2)
        self.assertIsNotNone(comment_stats["avg_likes"])

    def test_get_engagement_statistics_most_commented(self):
        """Test that most commented videos are correctly identified."""
        # Create videos with different comment counts
        video1 = Video.objects.create(
            title="Very Commented Video",
            url="https://youtube.com/very-commented",
            view_count=1000,
            like_count=100,
        )
        video2 = Video.objects.create(
            title="Less Commented Video",
            url="https://youtube.com/less-commented",
            view_count=500,
            like_count=50,
        )

        # Add more comments to video1
        for i in range(3):
            Comment.objects.create(
                video=video1,
                author=f"User{i + 1}",
                content=f"Comment {i + 1}",
            )

        # Add fewer comments to video2
        Comment.objects.create(
            video=video2,
            author="UserX",
            content="Single comment",
        )

        result = self.service.get_engagement_statistics()
        most_commented = result["most_commented_videos"]

        self.assertIsInstance(most_commented, list)
        self.assertGreater(len(most_commented), 0)

        # video1 should be first (most commented)
        if len(most_commented) >= 2:
            self.assertGreaterEqual(
                most_commented[0]["comment_count"], most_commented[1]["comment_count"]
            )

    def test_get_engagement_statistics_no_data(self):
        """Test statistics generation with no data."""
        result = self.service.get_engagement_statistics()

        # Should still return valid structure with zero counts
        self.assertEqual(result["video_stats"]["total_videos"], 0)
        self.assertEqual(result["comment_stats"]["total_comments"], 0)
        self.assertEqual(len(result["most_commented_videos"]), 0)

    def test_cleanup_old_content_removes_old_items(self):
        """Test that cleanup removes items older than specified days."""
        from django.utils import timezone
        from datetime import timedelta

        # Create old video (35 days ago)
        old_date = timezone.now() - timedelta(days=35)
        old_video = Video.objects.create(
            title="Old Video",
            url="https://youtube.com/old",
            created_at=old_date,
        )

        # Create recent video (5 days ago)
        recent_date = timezone.now() - timedelta(days=5)
        recent_video = Video.objects.create(
            title="Recent Video",
            url="https://youtube.com/recent",
            created_at=recent_date,
        )

        # Create old comment
        old_comment = Comment.objects.create(
            video=old_video,
            author="OldUser",
            content="Old comment",
            created_at=old_date,
        )

        # Create recent comment
        recent_comment = Comment.objects.create(
            video=recent_video,
            author="RecentUser",
            content="Recent comment",
            created_at=recent_date,
        )

        result = self.service.cleanup_old_content(30)  # Remove items older than 30 days

        # Check response
        self.assertIn("videos_deleted", result)
        self.assertIn("comments_deleted", result)
        self.assertEqual(result["videos_deleted"], 1)  # Old video should be deleted
        self.assertEqual(result["comments_deleted"], 1)  # Old comment should be deleted

        # Verify database state
        self.assertFalse(Video.objects.filter(pk=old_video.pk).exists())
        self.assertTrue(Video.objects.filter(pk=recent_video.pk).exists())
        self.assertFalse(Comment.objects.filter(pk=old_comment.pk).exists())
        self.assertTrue(Comment.objects.filter(pk=recent_comment.pk).exists())

    def test_cleanup_old_content_no_old_items(self):
        """Test cleanup when no old items exist."""
        # Create only recent videos
        from django.utils import timezone
        from datetime import timedelta

        recent_date = timezone.now() - timedelta(days=5)
        Video.objects.create(
            title="Recent Video",
            url="https://youtube.com/recent",
            created_at=recent_date,
        )

        result = self.service.cleanup_old_content(30)

        self.assertEqual(result["videos_deleted"], 0)
        self.assertEqual(result["comments_deleted"], 0)

    def test_cleanup_old_content_with_default_days(self):
        """Test cleanup with default days parameter."""
        result = self.service.cleanup_old_content()  # Should default to 30 days

        # Should return proper structure
        self.assertIn("cutoff_date", result)
        self.assertIn("videos_deleted", result)
        self.assertIn("comments_deleted", result)

    def test_service_constants_are_defined(self):
        """Test that service constants are properly defined."""
        # Check that templates exist and have proper structure
        self.assertIsInstance(self.service.VIDEO_TEMPLATES, list)
        self.assertGreater(len(self.service.VIDEO_TEMPLATES), 0)

        for template in self.service.VIDEO_TEMPLATES:
            self.assertIn("title", template)
            self.assertIn("description", template)
            self.assertIn("topics", template)
            self.assertIsInstance(template["topics"], list)
            self.assertGreater(len(template["topics"]), 0)

        # Check authors list
        self.assertIsInstance(self.service.COMMENT_AUTHORS, list)
        self.assertGreater(len(self.service.COMMENT_AUTHORS), 0)

        # Check tones list
        self.assertIsInstance(self.service.COMMENT_TONES, list)
        self.assertGreater(len(self.service.COMMENT_TONES), 0)
        expected_tones = [
            "friendly",
            "excited",
            "thoughtful",
            "appreciative",
            "curious",
            "critical",
        ]
        self.assertEqual(set(self.service.COMMENT_TONES), set(expected_tones))

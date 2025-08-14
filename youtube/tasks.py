"""
Celery tasks for scheduled content generation.
"""

import random
from celery import shared_task
from django.utils import timezone
import logging

from .services import ContentPopulationService

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def generate_video_content(self):
    """
    Generate a new video with realistic YouTube content.
    This simulates new content being uploaded to the platform.
    """
    try:
        content_service = ContentPopulationService()
        video_data = content_service.generate_video()

        logger.info(
            f"Generated new video: {video_data['title']} (ID: {video_data['video_id']})"
        )

        # Schedule comment generation for this video
        generate_comments_for_video.delay(
            video_data["video_id"], comment_count=random.randint(3, 8)
        )

        return {
            "video_id": video_data["video_id"],
            "title": video_data["title"],
            "message": "Video generated successfully",
        }

    except Exception as exc:
        logger.error(f"Error generating video content: {str(exc)}")
        raise self.retry(exc=exc)


@shared_task(bind=True, max_retries=3, default_retry_delay=30)
def generate_comments_for_video(self, video_id: int, comment_count: int = 5):
    """
    Generate AI-powered comments for a specific video.

    Args:
        video_id: ID of the video to generate comments for
        comment_count: Number of comments to generate
    """
    try:
        content_service = ContentPopulationService()
        result = content_service.generate_comments_for_video(video_id, comment_count)

        if "error" in result:
            logger.error(f"Video with ID {video_id} not found")
            return result

        logger.info(
            f"Generated {result['comments_generated']} comments for video {video_id}"
        )

        return {
            **result,
            "message": f"Generated {result['comments_generated']} comments successfully",
        }

    except Exception as exc:
        logger.error(f"Error generating comments for video {video_id}: {str(exc)}")
        raise self.retry(exc=exc)


@shared_task(bind=True, max_retries=2, default_retry_delay=120)
def simulate_user_engagement(self):
    """
    Simulate user engagement by randomly adding views, likes, and comments to existing videos.
    This makes the platform feel more alive with ongoing activity.
    """
    try:
        content_service = ContentPopulationService()
        result = content_service.simulate_engagement_for_videos()

        if result["videos_engaged"] == 0:
            logger.info("No videos found for engagement simulation")
            return result

        # Random chance to add a new comment (20% chance) for some videos
        for video_info in result["engagement_details"]:
            if random.random() < 0.2:
                generate_comments_for_video.delay(
                    video_info["video_id"], comment_count=1
                )
                video_info["activities"].append("scheduled +1 comment")

        logger.info(f"Simulated engagement for {result['videos_engaged']} videos")

        return {
            **result,
            "message": f"Simulated engagement for {result['videos_engaged']} videos",
        }

    except Exception as exc:
        logger.error(f"Error simulating user engagement: {str(exc)}")
        raise self.retry(exc=exc)


@shared_task(bind=True)
def cleanup_old_data(self, days_old: int = 30):
    """
    Clean up old test data to prevent database bloat.
    This is optional and can be used to maintain a reasonable data size.

    Args:
        days_old: Number of days after which to consider data old
    """
    try:
        content_service = ContentPopulationService()
        result = content_service.cleanup_old_content(days_old)

        logger.info(
            f"Cleanup completed: deleted {result['videos_deleted']} videos and {result['comments_deleted']} comments"
        )

        return {**result, "message": "Cleanup completed successfully"}

    except Exception as exc:
        logger.error(f"Error during cleanup: {str(exc)}")
        return {"error": str(exc)}


@shared_task
def generate_engagement_stats():
    """
    Generate and log engagement statistics for monitoring.
    This can be used for analytics and monitoring purposes.
    """
    try:
        content_service = ContentPopulationService()
        stats = content_service.get_engagement_statistics()

        stats["timestamp"] = timezone.now().isoformat()

        avg_views = stats["video_stats"]["avg_views"] or 0
        logger.info(
            f"Engagement stats: {stats['video_stats']['total_videos']} videos, "
            f"{stats['comment_stats']['total_comments']} comments, "
            f"avg {avg_views:.1f} views per video"
        )

        return stats

    except Exception as exc:
        logger.error(f"Error generating engagement stats: {str(exc)}")
        return {"error": str(exc)}

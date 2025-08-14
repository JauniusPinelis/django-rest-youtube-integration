"""
User engagement simulation tasks.
"""

import random
import logging
from celery import shared_task
from django.utils import timezone

from ..services import ContentPopulationService
from .base_task import BaseTask

logger = logging.getLogger(__name__)


class EngagementTasks(BaseTask):
    """Tasks related to user engagement simulation."""

    @staticmethod
    @shared_task(bind=True, max_retries=2, default_retry_delay=120)
    def simulate_user_engagement(self):
        """
        Simulate user engagement by randomly adding views, likes, and comments to existing videos.
        This makes the platform feel more alive with ongoing activity.
        """
        EngagementTasks.log_task_start("simulate_user_engagement", self.request.id)

        try:
            content_service = ContentPopulationService()
            result = content_service.simulate_engagement_for_videos()

            if result["videos_engaged"] == 0:
                logger.info("No videos found for engagement simulation")
                EngagementTasks.log_task_success(self.request.id, result)
                return result

            # Random chance to add a new comment (20% chance) for some videos
            from .content_generation_tasks import ContentGenerationTasks

            for video_info in result["engagement_details"]:
                if random.random() < 0.2:
                    ContentGenerationTasks.generate_comments_for_video.delay(
                        video_info["video_id"], comment_count=1
                    )
                    video_info["activities"].append("scheduled +1 comment")

            logger.info(f"Simulated engagement for {result['videos_engaged']} videos")

            final_result = {
                **result,
                "message": f"Simulated engagement for {result['videos_engaged']} videos",
            }

            EngagementTasks.log_task_success(self.request.id, final_result)
            return final_result

        except Exception as exc:
            error_msg = str(exc)
            logger.error(f"Error simulating user engagement: {error_msg}")
            EngagementTasks.log_task_retry(self.request.id, error_msg)
            raise self.retry(exc=exc)

    @staticmethod
    @shared_task(bind=True)
    def generate_engagement_stats(self):
        """
        Generate and log engagement statistics for monitoring.
        This can be used for analytics and monitoring purposes.
        """
        EngagementTasks.log_task_start("generate_engagement_stats", self.request.id)

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

            EngagementTasks.log_task_success(self.request.id, stats)
            return stats

        except Exception as exc:
            error_msg = str(exc)
            logger.error(f"Error generating engagement stats: {error_msg}")
            EngagementTasks.log_task_failure(self.request.id, error_msg)
            return {"error": error_msg}

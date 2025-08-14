"""
Content generation tasks for videos and comments.
"""

import random
import logging
from celery import shared_task

from ..services import ContentPopulationService
from .base_task import BaseTask

logger = logging.getLogger(__name__)


class ContentGenerationTasks(BaseTask):
    """Tasks related to content generation."""

    @staticmethod
    @shared_task(bind=True, max_retries=3, default_retry_delay=60)
    def generate_video_content(self):
        """
        Generate a new video with realistic YouTube content.
        This simulates new content being uploaded to the platform.
        """
        ContentGenerationTasks.log_task_start("generate_video_content", self.request.id)

        try:
            content_service = ContentPopulationService()
            video_data = content_service.generate_video()

            logger.info(
                f"Generated new video: {video_data['title']} (ID: {video_data['video_id']})"
            )

            # Schedule comment generation for this video
            ContentGenerationTasks.generate_comments_for_video.delay(
                video_data["video_id"], comment_count=random.randint(3, 8)
            )

            result = {
                "video_id": video_data["video_id"],
                "title": video_data["title"],
                "message": "Video generated successfully",
            }

            ContentGenerationTasks.log_task_success(self.request.id, result)
            return result

        except Exception as exc:
            error_msg = str(exc)
            logger.error(f"Error generating video content: {error_msg}")
            ContentGenerationTasks.log_task_retry(self.request.id, error_msg)
            raise self.retry(exc=exc)

    @staticmethod
    @shared_task(bind=True, max_retries=3, default_retry_delay=30)
    def generate_comments_for_video(self, video_id: int, comment_count: int = 5):
        """
        Generate AI-powered comments for a specific video.

        Args:
            video_id: ID of the video to generate comments for
            comment_count: Number of comments to generate
        """
        ContentGenerationTasks.log_task_start(
            "generate_comments_for_video",
            self.request.id,
            args=(video_id, comment_count),
        )

        try:
            content_service = ContentPopulationService()
            result = content_service.generate_comments_for_video(
                video_id, comment_count
            )

            if "error" in result:
                logger.error(f"Video with ID {video_id} not found")
                ContentGenerationTasks.log_task_failure(
                    self.request.id, f"Video with ID {video_id} not found"
                )
                return result

            logger.info(
                f"Generated {result['comments_generated']} comments for video {video_id}"
            )

            final_result = {
                **result,
                "message": f"Generated {result['comments_generated']} comments successfully",
            }

            ContentGenerationTasks.log_task_success(self.request.id, final_result)
            return final_result

        except Exception as exc:
            error_msg = str(exc)
            logger.error(f"Error generating comments for video {video_id}: {error_msg}")
            ContentGenerationTasks.log_task_retry(self.request.id, error_msg)
            raise self.retry(exc=exc)

    @staticmethod
    @shared_task(bind=True)
    def populate_initial_content(self):
        """
        Populate the platform with initial content on startup.
        This creates some videos and comments to make the platform feel active.
        """
        ContentGenerationTasks.log_task_start(
            "populate_initial_content", self.request.id
        )

        try:
            content_service = ContentPopulationService()

            # Generate initial videos
            video_count = random.randint(5, 10)
            videos_created = []

            for _ in range(video_count):
                video_data = content_service.generate_video()
                videos_created.append(video_data)

                # Generate comments for each video
                comment_count = random.randint(2, 5)
                content_service.generate_comments_for_video(
                    video_data["video_id"], comment_count
                )

            result = {
                "videos_created": len(videos_created),
                "video_ids": [v["video_id"] for v in videos_created],
                "message": f"Successfully populated {len(videos_created)} videos with comments",
            }

            logger.info(f"Initial population complete: {result['message']}")
            ContentGenerationTasks.log_task_success(self.request.id, result)
            return result

        except Exception as exc:
            error_msg = str(exc)
            logger.error(f"Error during initial population: {error_msg}")
            ContentGenerationTasks.log_task_failure(self.request.id, error_msg)
            return {"error": error_msg}

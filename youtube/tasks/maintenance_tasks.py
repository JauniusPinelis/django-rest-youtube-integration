"""
Maintenance and cleanup tasks.
"""

import logging
from celery import shared_task

from ..services import ContentPopulationService
from .base_task import BaseTask

logger = logging.getLogger(__name__)


class MaintenanceTasks(BaseTask):
    """Tasks related to system maintenance and cleanup."""

    @staticmethod
    @shared_task(bind=True)
    def cleanup_old_data(self, days_old: int = 30):
        """
        Clean up old test data to prevent database bloat.
        This is optional and can be used to maintain a reasonable data size.

        Args:
            days_old: Number of days after which to consider data old
        """
        MaintenanceTasks.log_task_start(
            "cleanup_old_data", self.request.id, kwargs={"days_old": days_old}
        )

        try:
            content_service = ContentPopulationService()
            result = content_service.cleanup_old_content(days_old)

            logger.info(
                f"Cleanup completed: deleted {result['videos_deleted']} videos "
                f"and {result['comments_deleted']} comments"
            )

            final_result = {**result, "message": "Cleanup completed successfully"}
            MaintenanceTasks.log_task_success(self.request.id, final_result)
            return final_result

        except Exception as exc:
            error_msg = str(exc)
            logger.error(f"Error during cleanup: {error_msg}")
            MaintenanceTasks.log_task_failure(self.request.id, error_msg)
            return {"error": error_msg}

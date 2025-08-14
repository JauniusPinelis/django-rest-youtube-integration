"""
Base task class with common functionality.
"""

import logging
from ..services.task_logging_service import TaskLoggingService

logger = logging.getLogger(__name__)


class BaseTask:
    """Base class for all task classes."""

    @staticmethod
    def log_task_start(
        task_name: str, task_id: str, args: tuple = None, kwargs: dict = None
    ):
        """Helper method to log task start."""
        return TaskLoggingService.log_task_start(task_name, task_id, args, kwargs)

    @staticmethod
    def log_task_success(task_id: str, result=None):
        """Helper method to log task success."""
        return TaskLoggingService.log_task_success(task_id, result)

    @staticmethod
    def log_task_failure(task_id: str, error_message: str):
        """Helper method to log task failure."""
        return TaskLoggingService.log_task_failure(task_id, error_message)

    @staticmethod
    def log_task_retry(task_id: str, error_message: str):
        """Helper method to log task retry."""
        return TaskLoggingService.log_task_retry(task_id, error_message)

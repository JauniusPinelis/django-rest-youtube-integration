"""
Task logging service for tracking Celery task execution.
"""

from typing import Any
from django.utils import timezone
from ..models import TaskLog


class TaskLoggingService:
    """Service for logging task execution to database."""

    @staticmethod
    def log_task_start(
        task_name: str, task_id: str, args: tuple = None, kwargs: dict = None
    ) -> TaskLog:
        """Log the start of a task execution."""
        return TaskLog.objects.create(
            task_name=task_name,
            task_id=task_id,
            status="PENDING",
            args=list(args) if args else None,
            kwargs=kwargs if kwargs else None,
            started_at=timezone.now(),
        )

    @staticmethod
    def log_task_success(task_id: str, result: Any = None) -> None:
        """Log successful task completion."""
        try:
            task_log = TaskLog.objects.get(task_id=task_id)
            task_log.status = "SUCCESS"
            task_log.result = result
            task_log.completed_at = timezone.now()

            if task_log.started_at:
                duration = (task_log.completed_at - task_log.started_at).total_seconds()
                task_log.duration_seconds = duration

            task_log.save()
        except TaskLog.DoesNotExist:
            pass

    @staticmethod
    def log_task_failure(task_id: str, error_message: str) -> None:
        """Log task failure."""
        try:
            task_log = TaskLog.objects.get(task_id=task_id)
            task_log.status = "FAILURE"
            task_log.error_message = error_message
            task_log.completed_at = timezone.now()

            if task_log.started_at:
                duration = (task_log.completed_at - task_log.started_at).total_seconds()
                task_log.duration_seconds = duration

            task_log.save()
        except TaskLog.DoesNotExist:
            pass

    @staticmethod
    def log_task_retry(task_id: str, error_message: str) -> None:
        """Log task retry attempt."""
        try:
            task_log = TaskLog.objects.get(task_id=task_id)
            task_log.status = "RETRY"
            task_log.error_message = error_message
            task_log.save()
        except TaskLog.DoesNotExist:
            pass

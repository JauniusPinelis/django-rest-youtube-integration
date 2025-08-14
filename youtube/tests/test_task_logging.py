"""
Tests for task logging functionality.
"""

from django.test import TestCase
from unittest.mock import patch
import uuid

from youtube.models import TaskLog
from youtube.services.task_logging_service import TaskLoggingService
from youtube.tasks import generate_engagement_stats


class TaskLogModelTest(TestCase):
    def test_task_log_creation(self):
        """Test TaskLog model creation."""
        task_log = TaskLog.objects.create(
            task_name="test_task", task_id="test-id-123", status="PENDING"
        )

        self.assertEqual(task_log.task_name, "test_task")
        self.assertEqual(task_log.task_id, "test-id-123")
        self.assertEqual(task_log.status, "PENDING")
        self.assertIsNone(task_log.result)


class TaskLoggingServiceTest(TestCase):
    def test_log_task_start(self):
        """Test logging task start."""
        task_id = str(uuid.uuid4())
        args = (1, 2, 3)
        kwargs = {"key": "value"}

        log = TaskLoggingService.log_task_start("test_task", task_id, args, kwargs)

        self.assertEqual(log.task_name, "test_task")
        self.assertEqual(log.task_id, task_id)
        self.assertEqual(log.status, "PENDING")
        self.assertEqual(log.args, [1, 2, 3])
        self.assertEqual(log.kwargs, {"key": "value"})

    def test_log_task_success(self):
        """Test logging task success."""
        task_id = str(uuid.uuid4())

        # Create initial log
        TaskLoggingService.log_task_start("test_task", task_id)

        # Log success
        result = {"message": "success"}
        TaskLoggingService.log_task_success(task_id, result)

        # Verify
        log = TaskLog.objects.get(task_id=task_id)
        self.assertEqual(log.status, "SUCCESS")
        self.assertEqual(log.result, result)
        self.assertIsNotNone(log.completed_at)
        self.assertIsNotNone(log.duration_seconds)

    def test_log_task_failure(self):
        """Test logging task failure."""
        task_id = str(uuid.uuid4())

        # Create initial log
        TaskLoggingService.log_task_start("test_task", task_id)

        # Log failure
        error_msg = "Something went wrong"
        TaskLoggingService.log_task_failure(task_id, error_msg)

        # Verify
        log = TaskLog.objects.get(task_id=task_id)
        self.assertEqual(log.status, "FAILURE")
        self.assertEqual(log.error_message, error_msg)
        self.assertIsNotNone(log.completed_at)


class TaskIntegrationTest(TestCase):
    @patch(
        "youtube.services.content_population_service.ContentPopulationService.get_engagement_statistics"
    )
    @patch("celery.Task.request")
    def test_task_with_logging(self, mock_request, mock_stats):
        """Test that tasks properly log their execution."""
        # Mock the task request
        task_id = str(uuid.uuid4())
        mock_request.id = task_id

        # Mock the service
        mock_stats.return_value = {
            "video_stats": {"total_videos": 5, "avg_views": 100},
            "comment_stats": {"total_comments": 15},
        }

        # Execute task directly (not via Celery)
        task_instance = generate_engagement_stats
        task_instance.request = mock_request

        task_instance()

        # Verify task log was created
        self.assertTrue(TaskLog.objects.filter(task_id=task_id).exists())

        log = TaskLog.objects.get(task_id=task_id)
        self.assertEqual(log.task_name, "generate_engagement_stats")
        self.assertEqual(log.status, "SUCCESS")
        self.assertIsNotNone(log.result)

"""
Django management command to set up Celery Beat periodic tasks.

This command creates the necessary periodic tasks for scheduled content generation.
It should be run after installing the application and migrating the database.

Usage:
    python manage.py setup_periodic_tasks
"""

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    help = """
    Set up Celery Beat periodic tasks for YouTube simulation.

    This command will create the following scheduled tasks:
    - Generate new video content (every 30 minutes)
    - Generate comments for existing videos (every 10 minutes) 
    - Simulate user engagement (every 5 minutes)
    - Generate engagement statistics (every hour)
    - Clean up old data (daily at 2 AM)
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear-existing",
            action="store_true",
            help="Clear existing periodic tasks before creating new ones",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        """Main command handler."""

        if options["clear_existing"]:
            self.stdout.write(self.style.WARNING("Clearing existing periodic tasks..."))
            self._clear_existing_tasks()

        self.stdout.write("Setting up periodic tasks for YouTube simulation...\n")

        try:
            # Create schedules
            schedules = self._create_schedules()

            # Create periodic tasks
            tasks_created = self._create_periodic_tasks(schedules, options)

            self.stdout.write(
                self.style.SUCCESS(
                    f"\nSuccessfully created {tasks_created} periodic tasks!"
                )
            )

            self.stdout.write("\nTo start the scheduler, run:")
            self.stdout.write(self.style.WARNING("celery -A youtube_api beat -l info"))

            self.stdout.write("\nTo start a worker, run:")
            self.stdout.write(
                self.style.WARNING("celery -A youtube_api worker -l info")
            )

        except Exception as e:
            raise CommandError(f"Error setting up periodic tasks: {str(e)}")

    def _clear_existing_tasks(self):
        """Clear existing periodic tasks and schedules."""
        # Delete existing YouTube-related periodic tasks
        deleted_tasks = PeriodicTask.objects.filter(
            name__startswith="YouTube:"
        ).delete()

        # Clean up unused schedules
        IntervalSchedule.objects.filter(periodictask__isnull=True).delete()
        CrontabSchedule.objects.filter(periodictask__isnull=True).delete()

        if deleted_tasks[0] > 0:
            self.stdout.write(
                self.style.WARNING(
                    f"Deleted {deleted_tasks[0]} existing periodic tasks"
                )
            )

    def _create_schedules(self):
        """Create and return schedule objects."""
        self.stdout.write("Creating schedules...")

        schedules = {}

        # Every 5 minutes - User engagement simulation
        schedules["every_5_minutes"], created = IntervalSchedule.objects.get_or_create(
            every=5,
            period=IntervalSchedule.MINUTES,
        )
        if created:
            self.stdout.write("  ✓ Created 5-minute interval schedule")

        # Every 10 minutes - Comment generation
        schedules["every_10_minutes"], created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.MINUTES,
        )
        if created:
            self.stdout.write("  ✓ Created 10-minute interval schedule")

        # Every 30 minutes - Video generation
        schedules["every_30_minutes"], created = IntervalSchedule.objects.get_or_create(
            every=30,
            period=IntervalSchedule.MINUTES,
        )
        if created:
            self.stdout.write("  ✓ Created 30-minute interval schedule")

        # Every hour - Statistics generation
        schedules["every_hour"], created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.HOURS,
        )
        if created:
            self.stdout.write("  ✓ Created hourly interval schedule")

        # Daily at 2 AM - Cleanup
        schedules["daily_2am"], created = CrontabSchedule.objects.get_or_create(
            minute=0,
            hour=2,
            day_of_week="*",
            day_of_month="*",
            month_of_year="*",
        )
        if created:
            self.stdout.write("  ✓ Created daily 2 AM crontab schedule")

        return schedules

    def _create_periodic_tasks(self, schedules, options):
        """Create periodic tasks using the provided schedules."""
        self.stdout.write("\nCreating periodic tasks...")

        tasks_created = 0

        # Task 1: Generate video content every 30 minutes
        task, created = PeriodicTask.objects.get_or_create(
            name="YouTube: Generate Video Content",
            defaults={
                "task": "youtube.tasks.generate_video_content",
                "interval": schedules["every_30_minutes"],
                "enabled": True,
                "description": "Generate new YouTube video content every 30 minutes",
            },
        )
        if created:
            self.stdout.write(
                "  ✓ Created video content generation task (every 30 minutes)"
            )
            tasks_created += 1

        # Task 2: Simulate user engagement every 5 minutes
        task, created = PeriodicTask.objects.get_or_create(
            name="YouTube: Simulate User Engagement",
            defaults={
                "task": "youtube.tasks.simulate_user_engagement",
                "interval": schedules["every_5_minutes"],
                "enabled": True,
                "description": "Simulate user engagement (views, likes) every 5 minutes",
            },
        )
        if created:
            self.stdout.write(
                "  ✓ Created user engagement simulation task (every 5 minutes)"
            )
            tasks_created += 1

        # Task 3: Generate engagement statistics every hour
        task, created = PeriodicTask.objects.get_or_create(
            name="YouTube: Generate Engagement Stats",
            defaults={
                "task": "youtube.tasks.generate_engagement_stats",
                "interval": schedules["every_hour"],
                "enabled": True,
                "description": "Generate and log engagement statistics every hour",
            },
        )
        if created:
            self.stdout.write("  ✓ Created engagement statistics task (every hour)")
            tasks_created += 1

        return tasks_created

    def _display_task_summary(self):
        """Display a summary of created tasks."""
        tasks = PeriodicTask.objects.filter(name__startswith="YouTube:")

        self.stdout.write("\nCreated periodic tasks:")
        for task in tasks:
            status = "✓ Enabled" if task.enabled else "✗ Disabled"
            if task.interval:
                schedule = f"every {task.interval.every} {task.interval.period}"
            elif task.crontab:
                schedule = f"cron: {task.crontab}"
            else:
                schedule = "No schedule"

            self.stdout.write(f"  {status} {task.name} ({schedule})")

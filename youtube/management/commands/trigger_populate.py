"""
Management command to manually trigger initial content population.
"""

from django.core.management.base import BaseCommand
from youtube.tasks import populate_initial_content


class Command(BaseCommand):
    help = "Trigger initial content population"

    def handle(self, *args, **options):
        self.stdout.write("Triggering initial content population...")

        result = populate_initial_content.delay()

        self.stdout.write(
            self.style.SUCCESS(f"Initial population task queued with ID: {result.id}")
        )
        self.stdout.write("Check the TaskLog in admin to see the results.")

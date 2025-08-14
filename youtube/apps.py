from django.apps import AppConfig


class YoutubeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "youtube"

    def ready(self):
        """Called when Django starts. Schedule initial population check."""
        import os
        import sys

        # Only run during runserver, not during migrations or other commands
        if os.environ.get("RUN_MAIN") == "true" and "runserver" in sys.argv:
            # Import here to avoid circular imports
            from threading import Timer

            def delayed_population_check():
                """Check if population is needed after Django is fully loaded."""
                try:
                    from .models import Video
                    from .tasks import populate_initial_content

                    # Only populate if there are no videos in the database
                    if Video.objects.count() == 0:
                        populate_initial_content.delay()
                except Exception as e:
                    print(f"Warning: Could not trigger initial population: {e}")

            # Schedule the check to run 2 seconds after Django starts
            Timer(2.0, delayed_population_check).start()

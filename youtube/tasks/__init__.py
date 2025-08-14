"""
Celery tasks for YouTube integration.
"""

from .content_generation_tasks import ContentGenerationTasks
from .engagement_tasks import EngagementTasks

# Export the task functions for backward compatibility
generate_video_content = ContentGenerationTasks.generate_video_content
generate_comments_for_video = ContentGenerationTasks.generate_comments_for_video
populate_initial_content = ContentGenerationTasks.populate_initial_content

simulate_user_engagement = EngagementTasks.simulate_user_engagement
generate_engagement_stats = EngagementTasks.generate_engagement_stats

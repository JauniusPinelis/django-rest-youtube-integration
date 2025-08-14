import os
import random
from django.db import transaction
from django.core.exceptions import ValidationError
from typing import Optional, List, Dict, Any
from openai import OpenAI
from .models import Video, Comment


class VideoService:
    """
    Service class for video-related operations.
    """

    @transaction.atomic
    def increment_views(self, *, video_id: int) -> Video:
        """
        Increment the view count for a video by 1.
        """
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        video.view_count += 1
        video.full_clean()
        video.save()

        return video

    @transaction.atomic
    def increment_likes(self, *, video_id: int) -> Video:
        """
        Increment the like count for a video by 1.
        """
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        video.like_count += 1
        video.full_clean()
        video.save()

        return video


class CommentService:
    """
    Service class for comment-related operations.
    """

    @transaction.atomic
    def create(self, *, video_id: int, author: str, content: str) -> Comment:
        """
        Create a new comment for a video.
        """
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        comment = Comment(video=video, author=author, content=content)
        comment.full_clean()
        comment.save()

        return comment

    @transaction.atomic
    def increment_likes(self, *, comment_id: int) -> Comment:
        """
        Increment the like count for a comment by 1.
        """
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            raise ValidationError("Comment not found.")

        comment.like_count += 1
        comment.full_clean()
        comment.save()

        return comment

    def get_by_video(self, *, video_id: Optional[int] = None):
        """
        Get comments, optionally filtered by video ID.
        """
        queryset = Comment.objects.all()
        if video_id is not None:
            queryset = queryset.filter(video=video_id)
        return queryset


class CommentGenerationService:
    """
    Service class for AI-powered comment generation using OpenAI.
    """

    def __init__(self, openai_client: Optional[OpenAI] = None):
        """
        Initialize the service with an OpenAI client.

        Args:
            openai_client: Optional OpenAI client instance. If not provided,
                         creates a new client using OPENAI_API_KEY environment variable.
        """
        if openai_client:
            self.client = openai_client
        else:
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                raise ValidationError("OPENAI_API_KEY environment variable is required")
            self.client = OpenAI(api_key=api_key)

    def generate_comment(
        self, *, video_title: str, video_description: str = "", tone: str = "friendly"
    ) -> str:
        """
        Generate a realistic comment for a video using OpenAI.

        Args:
            video_title: Title of the video
            video_description: Optional description of the video
            tone: Tone of the comment (friendly, excited, critical, thoughtful)

        Returns:
            Generated comment text

        Raises:
            ValidationError: If API call fails or returns invalid response
        """
        try:
            system_prompt = (
                "You are a YouTube viewer generating realistic comments. "
                "Create natural, authentic comments that people would actually write. "
                "Keep comments concise (1-3 sentences) and avoid overly promotional language."
            )

            user_prompt = f"Write a {tone} comment for a video titled '{video_title}'"
            if video_description:
                user_prompt += f" with description: {video_description[:200]}"

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=100,
                temperature=0.8,
            )

            if not response.choices or not response.choices[0].message.content:
                raise ValidationError("OpenAI API returned empty response")

            return response.choices[0].message.content.strip()

        except Exception as e:
            if isinstance(e, ValidationError):
                raise
            raise ValidationError(f"Failed to generate comment: {str(e)}")

    def generate_comments_bulk(
        self,
        *,
        video_title: str,
        video_description: str = "",
        count: int = 5,
        tones: Optional[List[str]] = None,
    ) -> List[str]:
        """
        Generate multiple comments for a video.

        Args:
            video_title: Title of the video
            video_description: Optional description of the video
            count: Number of comments to generate (max 10)
            tones: List of tones to use. If None, uses default varied tones

        Returns:
            List of generated comment texts

        Raises:
            ValidationError: If parameters are invalid or API calls fail
        """
        if count > 10:
            raise ValidationError("Cannot generate more than 10 comments at once")

        if not tones:
            tones = ["friendly", "excited", "thoughtful", "appreciative", "curious"]

        comments = []
        for i in range(count):
            tone = tones[i % len(tones)]
            comment = self.generate_comment(
                video_title=video_title, video_description=video_description, tone=tone
            )
            comments.append(comment)

        return comments

    @transaction.atomic
    def generate_and_save_comment(
        self, *, video_id: int, author: str = "AI User", tone: str = "friendly"
    ) -> Comment:
        """
        Generate a comment using AI and save it to the database.

        Args:
            video_id: ID of the video to comment on
            author: Author name for the comment
            tone: Tone of the comment

        Returns:
            Created Comment instance

        Raises:
            ValidationError: If video not found or generation fails
        """
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        generated_content = self.generate_comment(
            video_title=video.title, video_description=video.description, tone=tone
        )

        comment_service = CommentService()
        return comment_service.create(
            video_id=video_id, author=author, content=generated_content
        )


class ContentPopulationService:
    """
    Service class for generating realistic content for platform population.
    Handles video creation, comment generation, and engagement simulation.
    """

    def __init__(self):
        self.video_service = VideoService()
        self.comment_service = CommentService()
        self.comment_generator = CommentGenerationService()

    # Video content templates and data
    VIDEO_TEMPLATES = [
        {
            "title": "Amazing Python Tutorial: {topic}",
            "description": "Learn {topic} in this comprehensive tutorial. Perfect for beginners and advanced developers alike!",
            "topics": [
                "Django Rest Framework",
                "Async Programming",
                "Data Science",
                "Machine Learning",
                "Web Scraping",
                "APIs",
            ],
        },
        {
            "title": "Daily Coding Challenge: {topic}",
            "description": "Today's coding challenge focuses on {topic}. Can you solve it?",
            "topics": [
                "Binary Trees",
                "Dynamic Programming",
                "Algorithms",
                "System Design",
                "Database Optimization",
            ],
        },
        {
            "title": "Tech News Update: {topic}",
            "description": "Latest updates about {topic} in the tech world. Stay informed!",
            "topics": [
                "AI Developments",
                "Cybersecurity",
                "Cloud Computing",
                "Mobile Development",
                "DevOps",
            ],
        },
        {
            "title": "Building Projects with {topic}",
            "description": "Step-by-step guide to building amazing projects using {topic}.",
            "topics": ["React", "Node.js", "Docker", "Kubernetes", "Microservices"],
        },
    ]

    COMMENT_AUTHORS = [
        "TechEnthusiast2024",
        "CodeMaster",
        "LearnWithMe",
        "DevLife",
        "PythonGuru",
        "WebDevPro",
        "DataScientist",
        "AIExplorer",
        "CloudExpert",
        "StartupFounder",
        "IndieHacker",
        "OpenSourceFan",
        "CodingBootcamp",
        "SoftwareArchitect",
        "MLEngineer",
    ]

    COMMENT_TONES = [
        "friendly",
        "excited",
        "thoughtful",
        "appreciative",
        "curious",
        "critical",
    ]

    @transaction.atomic
    def generate_video(self) -> Dict[str, Any]:
        """
        Generate a new video with realistic content and metadata.

        Returns:
            Dictionary containing video information and creation status
        """
        # Select random template and topic
        template = random.choice(self.VIDEO_TEMPLATES)
        topic = random.choice(template["topics"])

        # Generate video data
        title = template["title"].format(topic=topic)
        description = template["description"].format(topic=topic)

        # Generate realistic video metrics
        duration = random.randint(300, 3600)  # 5 minutes to 1 hour
        view_count = random.randint(100, 10000)
        like_count = random.randint(10, int(view_count * 0.1))

        # Generate a realistic URL
        video_id = f"dQw4w9WgXcQ_{random.randint(1000, 9999)}"
        url = f"https://youtube.com/watch?v={video_id}"
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

        # Create video
        video = Video.objects.create(
            title=title,
            description=description,
            url=url,
            thumbnail_url=thumbnail_url,
            duration=duration,
            view_count=view_count,
            like_count=like_count,
        )

        return {
            "video_id": video.id,
            "title": title,
            "description": description,
            "url": url,
            "duration": duration,
            "view_count": view_count,
            "like_count": like_count,
        }

    def generate_comments_for_video(
        self, video_id: int, comment_count: int = 5
    ) -> Dict[str, Any]:
        """
        Generate AI-powered comments for a specific video.

        Args:
            video_id: ID of the video to generate comments for
            comment_count: Number of comments to generate

        Returns:
            Dictionary containing comment generation results
        """
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            return {"error": "Video not found"}

        generated_comments = []

        for i in range(comment_count):
            try:
                # Select random author and tone
                author = random.choice(self.COMMENT_AUTHORS)
                tone = random.choice(self.COMMENT_TONES)

                # Generate comment content using AI
                content = self.comment_generator.generate_comment(
                    video_title=video.title,
                    video_description=video.description[:200],
                    tone=tone,
                )

                # Create comment
                comment = self.comment_service.create(
                    video_id=video_id, author=author, content=content
                )

                # Add some random likes to the comment
                comment.like_count = random.randint(0, 50)
                comment.save()

                generated_comments.append(
                    {
                        "comment_id": comment.id,
                        "author": author,
                        "content": content[:50] + "..."
                        if len(content) > 50
                        else content,
                        "tone": tone,
                    }
                )

            except (ValidationError, Exception):
                # Continue with other comments if one fails
                continue

        return {
            "video_id": video_id,
            "video_title": video.title,
            "comments_generated": len(generated_comments),
            "comments": generated_comments,
        }

    def simulate_engagement_for_videos(
        self, video_count: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Simulate user engagement for random videos.

        Args:
            video_count: Number of videos to engage with. If None, uses random 3-8

        Returns:
            Dictionary containing engagement simulation results
        """
        if video_count is None:
            video_count = random.randint(3, 8)

        # Get random videos to engage with
        videos = list(Video.objects.all().order_by("?")[:video_count])

        if not videos:
            return {
                "message": "No videos available for engagement",
                "videos_engaged": 0,
            }

        engagement_results = []

        for video in videos:
            try:
                activities = []

                # Random chance to add views (70% chance)
                if random.random() < 0.7:
                    views_to_add = random.randint(1, 50)
                    for _ in range(views_to_add):
                        self.video_service.increment_views(video_id=video.id)
                    activities.append(f"+{views_to_add} views")

                # Random chance to add likes (30% chance)
                if random.random() < 0.3:
                    likes_to_add = random.randint(1, 5)
                    for _ in range(likes_to_add):
                        self.video_service.increment_likes(video_id=video.id)
                    activities.append(f"+{likes_to_add} likes")

                engagement_results.append(
                    {
                        "video_id": video.id,
                        "video_title": video.title[:30] + "..."
                        if len(video.title) > 30
                        else video.title,
                        "activities": activities,
                    }
                )

            except (ValidationError, Exception):
                # Continue with other videos if one fails
                continue

        return {
            "videos_engaged": len(engagement_results),
            "engagement_details": engagement_results,
        }

    def get_engagement_statistics(self) -> Dict[str, Any]:
        """
        Generate engagement statistics for monitoring.

        Returns:
            Dictionary containing platform statistics
        """
        from django.db.models import Count, Avg, Max

        # Get video statistics
        video_stats = Video.objects.aggregate(
            total_videos=Count("id"),
            avg_views=Avg("view_count"),
            avg_likes=Avg("like_count"),
            max_views=Max("view_count"),
            max_likes=Max("like_count"),
        )

        # Get comment statistics
        comment_stats = Comment.objects.aggregate(
            total_comments=Count("id"),
            avg_likes=Avg("like_count"),
        )

        # Get most commented videos
        most_commented = list(
            Video.objects.annotate(comment_count=Count("comments"))
            .order_by("-comment_count")[:5]
            .values("id", "title", "comment_count", "view_count", "like_count")
        )

        return {
            "video_stats": video_stats,
            "comment_stats": comment_stats,
            "most_commented_videos": most_commented,
        }

    def cleanup_old_content(self, days_old: int = 30) -> Dict[str, Any]:
        """
        Clean up old content to prevent database bloat.

        Args:
            days_old: Number of days after which to consider content old

        Returns:
            Dictionary containing cleanup results
        """
        from datetime import timedelta
        from django.utils import timezone

        cutoff_date = timezone.now() - timedelta(days=days_old)

        # Count items to be deleted (not used but kept for potential logging)

        # Delete old data
        deleted_comments = Comment.objects.filter(created_at__lt=cutoff_date).delete()
        deleted_videos = Video.objects.filter(created_at__lt=cutoff_date).delete()

        return {
            "videos_deleted": deleted_videos[0] if deleted_videos[0] else 0,
            "comments_deleted": deleted_comments[0] if deleted_comments[0] else 0,
            "cutoff_date": cutoff_date.isoformat(),
        }

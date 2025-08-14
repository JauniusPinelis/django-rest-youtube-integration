import random
from django.db import transaction
from django.core.exceptions import ValidationError
from typing import Optional, Dict, Any
from ..models import Video, Comment
from .video_service import VideoService
from .comment_service import CommentService
from .comment_generation_service import CommentGenerationService


class ContentPopulationService:
    def __init__(self):
        self.video_service = VideoService()
        self.comment_service = CommentService()
        self.comment_generator = CommentGenerationService()

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
        template = random.choice(self.VIDEO_TEMPLATES)
        topic = random.choice(template["topics"])

        title = template["title"].format(topic=topic)
        description = template["description"].format(topic=topic)

        duration = random.randint(300, 3600)
        view_count = random.randint(100, 10000)
        like_count = random.randint(10, int(view_count * 0.1))

        video_id = f"dQw4w9WgXcQ_{random.randint(1000, 9999)}"
        url = f"https://youtube.com/watch?v={video_id}"
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

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
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            return {"error": "Video not found"}

        generated_comments = []

        for i in range(comment_count):
            try:
                author = random.choice(self.COMMENT_AUTHORS)
                tone = random.choice(self.COMMENT_TONES)

                content = self.comment_generator.generate_comment(
                    video_title=video.title,
                    video_description=video.description[:200],
                    tone=tone,
                )

                comment = self.comment_service.create(
                    video_id=video_id, author=author, content=content
                )

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
        if video_count is None:
            video_count = random.randint(3, 8)

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

                if random.random() < 0.7:
                    views_to_add = random.randint(1, 50)
                    for _ in range(views_to_add):
                        self.video_service.increment_views(video_id=video.id)
                    activities.append(f"+{views_to_add} views")

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
                continue

        return {
            "videos_engaged": len(engagement_results),
            "engagement_details": engagement_results,
        }

    def get_engagement_statistics(self) -> Dict[str, Any]:
        from django.db.models import Count, Avg, Max

        video_stats = Video.objects.aggregate(
            total_videos=Count("id"),
            avg_views=Avg("view_count"),
            avg_likes=Avg("like_count"),
            max_views=Max("view_count"),
            max_likes=Max("like_count"),
        )

        comment_stats = Comment.objects.aggregate(
            total_comments=Count("id"),
            avg_likes=Avg("like_count"),
        )

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
        from datetime import timedelta
        from django.utils import timezone

        cutoff_date = timezone.now() - timedelta(days=days_old)

        deleted_comments = Comment.objects.filter(created_at__lt=cutoff_date).delete()
        deleted_videos = Video.objects.filter(created_at__lt=cutoff_date).delete()

        return {
            "videos_deleted": deleted_videos[0] if deleted_videos[0] else 0,
            "comments_deleted": deleted_comments[0] if deleted_comments[0] else 0,
            "cutoff_date": cutoff_date.isoformat(),
        }
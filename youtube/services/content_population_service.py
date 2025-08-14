import os
import random
from django.db import transaction
from django.core.exceptions import ValidationError
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from openai import OpenAI
from ..models import Video, Comment
from .video_service import VideoService
from .comment_service import CommentService


class GeneratedComment(BaseModel):
    content: str = Field(description="The comment text content")
    tone: str = Field(
        description="The tone of the comment (friendly, excited, thoughtful, etc.)"
    )
    author_style: str = Field(
        description="The style this author typically uses (casual, technical, enthusiastic, etc.)"
    )


class CommentBatch(BaseModel):
    comments: List[GeneratedComment] = Field(description="List of generated comments")


class ContentPopulationService:
    def __init__(self):
        self.video_service = VideoService()
        self.comment_service = CommentService()

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValidationError("OPENAI_API_KEY environment variable is required")
        self.client = OpenAI(api_key=api_key)

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

    def _generate_comments_with_ai(
        self, video_title: str, video_description: str, comment_count: int
    ) -> List[GeneratedComment]:
        """Generate comments using OpenAI GPT-5 with structured output"""
        try:
            system_prompt = (
                "You are a YouTube comment generator. Create realistic, diverse comments "
                "that real users would write. Vary the tone and author style for each comment. "
                "Keep comments authentic and concise (1-3 sentences)."
            )

            user_prompt = f"""Generate {comment_count} diverse comments for this video:
Title: {video_title}
Description: {video_description[:200]}

Create comments with different tones like: {", ".join(self.COMMENT_TONES)}
Vary the author styles and perspectives."""

            response = self.client.beta.chat.completions.parse(
                model="gpt-5",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                response_format=CommentBatch,
                temperature=0.8,
            )

            if response.choices and response.choices[0].message.parsed:
                return response.choices[0].message.parsed.comments
            else:
                raise ValidationError("OpenAI API returned empty response")

        except Exception as e:
            raise ValidationError(f"Failed to generate comments: {str(e)}")

    def generate_comments_for_video(
        self, video_id: int, comment_count: int = 5
    ) -> Dict[str, Any]:
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            return {"error": "Video not found"}

        generated_comments = []

        try:
            # Generate comments using structured AI output
            ai_comments = self._generate_comments_with_ai(
                video.title, video.description, comment_count
            )

            for ai_comment in ai_comments:
                author = random.choice(self.COMMENT_AUTHORS)

                comment = self.comment_service.create(
                    video_id=video_id, author=author, content=ai_comment.content
                )

                comment.like_count = random.randint(0, 50)
                comment.save()

                generated_comments.append(
                    {
                        "comment_id": comment.id,
                        "author": author,
                        "content": ai_comment.content[:50] + "..."
                        if len(ai_comment.content) > 50
                        else ai_comment.content,
                        "tone": ai_comment.tone,
                        "author_style": ai_comment.author_style,
                    }
                )

        except (ValidationError, Exception):
            # Fallback to simpler method if structured output fails
            for i in range(comment_count):
                try:
                    author = random.choice(self.COMMENT_AUTHORS)
                    tone = random.choice(self.COMMENT_TONES)

                    # Simple fallback comment generation
                    content = (
                        f"Great {tone} video about {video.title}! Thanks for sharing."
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
                            "content": content,
                            "tone": tone,
                            "author_style": "fallback",
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

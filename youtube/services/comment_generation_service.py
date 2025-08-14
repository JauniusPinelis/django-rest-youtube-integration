import os
from django.db import transaction
from django.core.exceptions import ValidationError
from typing import Optional, List
from openai import OpenAI
from ..models import Video, Comment
from .comment_service import CommentService


class CommentGenerationService:
    def __init__(self, openai_client: Optional[OpenAI] = None):
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

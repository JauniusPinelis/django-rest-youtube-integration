from django.db import transaction
from django.core.exceptions import ValidationError
from typing import Optional
from ..models import Video, Comment


class CommentService:
    @transaction.atomic
    def create(self, *, video_id: int, author: str, content: str) -> Comment:
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
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            raise ValidationError("Comment not found.")

        comment.like_count += 1
        comment.full_clean()
        comment.save()

        return comment

    def get_by_video(self, *, video_id: Optional[int] = None):
        queryset = Comment.objects.all()
        if video_id is not None:
            queryset = queryset.filter(video=video_id)
        return queryset
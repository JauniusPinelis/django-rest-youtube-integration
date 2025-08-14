from django.db import transaction
from django.core.exceptions import ValidationError
from django.db.models import Count
from typing import Optional
from ..models import Video


class VideoService:
    def get_all(self):
        return Video.objects.annotate(comments_count=Count("comments")).all()

    def get_by_id(self, *, video_id: int) -> Video:
        try:
            return (
                Video.objects.select_related()
                .prefetch_related("comments")
                .annotate(comments_count=Count("comments"))
                .get(pk=video_id)
            )
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

    @transaction.atomic
    def create(
        self,
        *,
        title: str,
        description: str = "",
        url: str,
        thumbnail_url: Optional[str] = None,
        duration: Optional[int] = None,
    ) -> Video:
        video = Video(
            title=title,
            description=description,
            url=url,
            thumbnail_url=thumbnail_url,
            duration=duration,
        )
        video.full_clean()
        video.save()

        # Return with annotations for serializer compatibility
        return Video.objects.annotate(comments_count=Count("comments")).get(pk=video.pk)

    @transaction.atomic
    def update(self, *, video_id: int, **kwargs) -> Video:
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        for field, value in kwargs.items():
            setattr(video, field, value)

        video.full_clean()
        video.save()

        # Return with annotations for serializer compatibility
        return (
            Video.objects.select_related()
            .prefetch_related("comments")
            .annotate(comments_count=Count("comments"))
            .get(pk=video.pk)
        )

    @transaction.atomic
    def delete(self, *, video_id: int) -> None:
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        video.delete()

    @transaction.atomic
    def increment_views(self, *, video_id: int) -> Video:
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
        try:
            video = Video.objects.get(pk=video_id)
        except Video.DoesNotExist:
            raise ValidationError("Video not found.")

        video.like_count += 1
        video.full_clean()
        video.save()

        return video

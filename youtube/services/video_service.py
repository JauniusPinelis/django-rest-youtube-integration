from django.db import transaction
from django.core.exceptions import ValidationError
from ..models import Video


class VideoService:
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
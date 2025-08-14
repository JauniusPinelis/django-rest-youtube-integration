from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import serializers as drf_serializers
from .models import Video
from .serializers import VideoSerializer, VideoListSerializer, CommentSerializer
from .services import VideoService, CommentService


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_service = VideoService()

    def get_serializer_class(self):
        if self.action == "list":
            return VideoListSerializer
        return VideoSerializer

    @action(detail=True, methods=["post"])
    def increment_views(self, request, pk=None):
        try:
            video = self.video_service.increment_views(video_id=pk)
            return Response({"view_count": video.view_count})
        except ValidationError as e:
            raise drf_serializers.ValidationError({"detail": str(e)})

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        try:
            video = self.video_service.increment_likes(video_id=pk)
            return Response({"like_count": video.like_count})
        except ValidationError as e:
            raise drf_serializers.ValidationError({"detail": str(e)})


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comment_service = CommentService()

    def get_queryset(self):
        video_id = self.request.query_params.get("video", None)
        if video_id is not None:
            video_id = int(video_id)
        return self.comment_service.get_by_video(video_id=video_id)

    def perform_create(self, serializer):
        video_id = self.request.data.get("video")
        author = self.request.data.get("author")
        content = self.request.data.get("content")

        try:
            comment = self.comment_service.create(
                video_id=video_id, author=author, content=content
            )
            # We need to prevent the default save since we already created the comment
            serializer.instance = comment
        except ValidationError as e:
            raise drf_serializers.ValidationError({"video": str(e)})

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        try:
            comment = self.comment_service.increment_likes(comment_id=pk)
            return Response({"like_count": comment.like_count})
        except ValidationError as e:
            raise drf_serializers.ValidationError({"detail": str(e)})

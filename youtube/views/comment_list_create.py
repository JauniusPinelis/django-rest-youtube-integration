from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from youtube.services.comment_service import CommentService
from .base import StandardResultsSetPagination


class CommentListCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        video = serializers.IntegerField()
        author = serializers.CharField(max_length=100)
        content = serializers.CharField()

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        video = serializers.SerializerMethodField()
        author = serializers.CharField()
        content = serializers.CharField()
        like_count = serializers.IntegerField()
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()

        def get_video(self, obj):
            return obj.video.id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comment_service = CommentService()

    def get(self, request):
        video_id = request.query_params.get("video", None)
        if video_id is not None:
            video_id = int(video_id)

        comments = self.comment_service.get_by_video(video_id=video_id)

        paginator = StandardResultsSetPagination()
        paginated_comments = paginator.paginate_queryset(comments, request)
        serializer = self.OutputSerializer(paginated_comments, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Convert video to video_id for the service
        validated_data = serializer.validated_data.copy()
        validated_data["video_id"] = validated_data.pop("video")
        comment = self.comment_service.create(**validated_data)

        output_serializer = self.OutputSerializer(comment)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

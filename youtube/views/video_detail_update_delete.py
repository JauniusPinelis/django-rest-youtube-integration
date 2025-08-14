from .base import APIView, Response, status, serializers, VideoService


class VideoDetailUpdateDeleteAPI(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=200, required=False)
        description = serializers.CharField(required=False, allow_blank=True)
        url = serializers.URLField(required=False)
        thumbnail_url = serializers.URLField(required=False, allow_null=True)
        duration = serializers.IntegerField(required=False, allow_null=True)

    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        description = serializers.CharField()
        url = serializers.URLField()
        thumbnail_url = serializers.URLField(allow_null=True)
        duration = serializers.IntegerField(allow_null=True)
        view_count = serializers.IntegerField()
        like_count = serializers.IntegerField()
        created_at = serializers.DateTimeField()
        updated_at = serializers.DateTimeField()
        comments = serializers.SerializerMethodField()
        comments_count = serializers.IntegerField()

        def get_comments(self, obj):
            from .comment_detail_update_delete import CommentDetailUpdateDeleteAPI

            return CommentDetailUpdateDeleteAPI.OutputSerializer(
                obj.comments.all(), many=True
            ).data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_service = VideoService()

    def get(self, request, pk):
        video = self.video_service.get_by_id(video_id=pk)
        serializer = self.OutputSerializer(video)
        return Response(serializer.data)

    def put(self, request, pk):
        self.video_service.get_by_id(video_id=pk)

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = self.video_service.update(video_id=pk, **serializer.validated_data)

        output_serializer = self.OutputSerializer(video)
        return Response(output_serializer.data)

    def patch(self, request, pk):
        self.video_service.get_by_id(video_id=pk)

        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        video = self.video_service.update(video_id=pk, **serializer.validated_data)

        output_serializer = self.OutputSerializer(video)
        return Response(output_serializer.data)

    def delete(self, request, pk):
        self.video_service.delete(video_id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

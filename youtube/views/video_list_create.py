from .base import (
    APIView,
    Response,
    status,
    serializers,
    StandardResultsSetPagination,
    VideoService,
)


class VideoListCreateAPI(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=200)
        description = serializers.CharField(allow_blank=True)
        url = serializers.URLField()
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
        comments_count = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_service = VideoService()

    def get(self, request):
        videos = self.video_service.get_all()

        paginator = StandardResultsSetPagination()
        paginated_videos = paginator.paginate_queryset(videos, request)
        serializer = self.OutputSerializer(paginated_videos, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = self.video_service.create(**serializer.validated_data)

        output_serializer = self.OutputSerializer(video)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

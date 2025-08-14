from .base import (
    APIView, Response, status, serializers, ValidationError, VideoService
)


class VideoIncrementViewsAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        view_count = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_service = VideoService()

    def post(self, request, pk):
        try:
            video = self.video_service.increment_views(video_id=pk)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.OutputSerializer({"view_count": video.view_count})
        return Response(serializer.data)
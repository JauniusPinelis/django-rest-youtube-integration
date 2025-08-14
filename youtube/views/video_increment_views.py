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
        video = self.video_service.increment_views(video_id=pk)
        serializer = self.OutputSerializer({"view_count": video.view_count})
        return Response(serializer.data)
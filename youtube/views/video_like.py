from .base import (
    APIView, Response, status, serializers, ValidationError, VideoService
)


class VideoLikeAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        like_count = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_service = VideoService()

    def post(self, request, pk):
        video = self.video_service.increment_likes(video_id=pk)
        serializer = self.OutputSerializer({"like_count": video.like_count})
        return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from youtube.services.video_service import VideoService


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

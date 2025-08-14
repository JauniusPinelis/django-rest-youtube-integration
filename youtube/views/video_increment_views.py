from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from youtube.services.video_service import VideoService


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

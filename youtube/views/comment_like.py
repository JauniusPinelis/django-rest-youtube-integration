from .base import (
    APIView, Response, status, serializers, ValidationError, CommentService
)


class CommentLikeAPI(APIView):
    class OutputSerializer(serializers.Serializer):
        like_count = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comment_service = CommentService()

    def post(self, request, pk):
        comment = self.comment_service.increment_likes(comment_id=pk)
        serializer = self.OutputSerializer({"like_count": comment.like_count})
        return Response(serializer.data)
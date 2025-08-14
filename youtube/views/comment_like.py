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
        try:
            comment = self.comment_service.increment_likes(comment_id=pk)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.OutputSerializer({"like_count": comment.like_count})
        return Response(serializer.data)
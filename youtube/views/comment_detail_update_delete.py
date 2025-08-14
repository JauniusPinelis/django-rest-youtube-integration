from .base import (
    APIView, Response, status, serializers, ValidationError, Http404, CommentService
)


class CommentDetailUpdateDeleteAPI(APIView):
    class InputSerializer(serializers.Serializer):
        author = serializers.CharField(max_length=100, required=False)
        content = serializers.CharField(required=False)

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

    def get(self, request, pk):
        comment = self.comment_service.get_by_id(comment_id=pk)
        serializer = self.OutputSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        self.comment_service.get_by_id(comment_id=pk)

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = self.comment_service.update(comment_id=pk, **serializer.validated_data)

        output_serializer = self.OutputSerializer(comment)
        return Response(output_serializer.data)

    def patch(self, request, pk):
        self.comment_service.get_by_id(comment_id=pk)

        serializer = self.InputSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        comment = self.comment_service.update(comment_id=pk, **serializer.validated_data)

        output_serializer = self.OutputSerializer(comment)
        return Response(output_serializer.data)

    def delete(self, request, pk):
        self.comment_service.delete(comment_id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
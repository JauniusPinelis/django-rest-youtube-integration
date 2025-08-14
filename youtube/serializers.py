from rest_framework import serializers
from .models import Video, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "video",
            "author",
            "content",
            "like_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class VideoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "description",
            "url",
            "thumbnail_url",
            "duration",
            "view_count",
            "like_count",
            "created_at",
            "updated_at",
            "comments",
            "comments_count",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_comments_count(self, obj):
        return obj.comments.count()


class VideoListSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "description",
            "url",
            "thumbnail_url",
            "duration",
            "view_count",
            "like_count",
            "created_at",
            "comments_count",
        ]
        read_only_fields = ["id", "created_at"]

    def get_comments_count(self, obj):
        return obj.comments.count()

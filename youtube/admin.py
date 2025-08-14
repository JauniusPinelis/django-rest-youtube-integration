from django.contrib import admin
from .models import Video, Comment


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["title", "view_count", "like_count", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "video", "like_count", "created_at"]
    list_filter = ["created_at", "video"]
    search_fields = ["author", "content"]
    readonly_fields = ["created_at", "updated_at"]

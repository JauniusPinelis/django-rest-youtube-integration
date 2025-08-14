from django.contrib import admin
from .models import Video, Comment, TaskLog


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


@admin.register(TaskLog)
class TaskLogAdmin(admin.ModelAdmin):
    list_display = [
        "task_name",
        "status",
        "started_at",
        "completed_at",
        "duration_seconds",
    ]
    list_filter = ["status", "task_name", "started_at"]
    search_fields = ["task_name", "task_id", "error_message"]
    readonly_fields = ["task_id", "started_at", "completed_at", "duration_seconds"]
    date_hierarchy = "started_at"

    fieldsets = (
        ("Task Info", {"fields": ("task_name", "task_id", "status")}),
        ("Execution", {"fields": ("started_at", "completed_at", "duration_seconds")}),
        ("Parameters", {"fields": ("args", "kwargs"), "classes": ("collapse",)}),
        ("Results", {"fields": ("result", "error_message"), "classes": ("collapse",)}),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

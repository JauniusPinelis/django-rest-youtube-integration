from django.urls import path
from .views import (
    VideoListCreateAPI,
    VideoDetailUpdateDeleteAPI,
    VideoIncrementViewsAPI,
    VideoLikeAPI,
    CommentListCreateAPI,
    CommentDetailUpdateDeleteAPI,
    CommentLikeAPI,
)

urlpatterns = [
    # Video URLs
    path("api/videos/", VideoListCreateAPI.as_view(), name="video-list"),
    path(
        "api/videos/<int:pk>/",
        VideoDetailUpdateDeleteAPI.as_view(),
        name="video-detail",
    ),
    path(
        "api/videos/<int:pk>/increment_views/",
        VideoIncrementViewsAPI.as_view(),
        name="video-increment-views",
    ),
    path("api/videos/<int:pk>/like/", VideoLikeAPI.as_view(), name="video-like"),
    # Comment URLs
    path("api/comments/", CommentListCreateAPI.as_view(), name="comment-list"),
    path(
        "api/comments/<int:pk>/",
        CommentDetailUpdateDeleteAPI.as_view(),
        name="comment-detail",
    ),
    path("api/comments/<int:pk>/like/", CommentLikeAPI.as_view(), name="comment-like"),
]

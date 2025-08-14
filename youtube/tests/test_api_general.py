"""
API integration tests for error handling.

These tests focus on API error responses and validation.
"""

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class APIErrorHandlingTest(APITestCase):
    """Test suite for API error handling."""

    def setUp(self):
        """Set up test client for error handling tests."""
        self.client = APIClient()

    def test_invalid_video_id_format_returns_404(self):
        """Test API response for invalid ID format returns 404"""
        url = "/api/videos/invalid-id/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_empty_request_body_returns_validation_errors(self):
        """Test empty POST request returns field validation errors"""
        url = reverse("video-list")
        response = self.client.post(url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertIn("url", response.data)

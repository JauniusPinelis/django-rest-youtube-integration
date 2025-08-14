from django.test import TestCase
from django.core.exceptions import (
    ValidationError as DjangoValidationError,
    PermissionDenied,
)
from django.http import Http404
from rest_framework import exceptions, status
from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView
from rest_framework.response import Response

from youtube.exceptions import drf_default_with_modifications_exception_handler


class TestExceptionHandlerView(APIView):
    def get(self, request):
        exception_type = request.GET.get("exception_type")

        if exception_type == "django_validation":
            raise DjangoValidationError("Django validation error")
        elif exception_type == "http404":
            raise Http404("Not found")
        elif exception_type == "permission_denied":
            raise PermissionDenied("Permission denied")
        elif exception_type == "drf_validation":
            raise exceptions.ValidationError({"field": ["This field is required."]})
        elif exception_type == "unexpected":
            raise Exception("Unexpected error")

        return Response({"success": True})


class CustomExceptionHandlerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TestExceptionHandlerView.as_view()

    def test_django_validation_error_conversion(self):
        """Test that Django ValidationError is converted to DRF ValidationError with detail wrapper"""
        request = self.factory.get("/", {"exception_type": "django_validation"})
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_http404_conversion(self):
        """Test that Http404 is converted to DRF NotFound with detail wrapper"""
        request = self.factory.get("/", {"exception_type": "http404"})
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data)

    def test_permission_denied_conversion(self):
        """Test that PermissionDenied is converted to DRF PermissionDenied with detail wrapper"""
        request = self.factory.get("/", {"exception_type": "permission_denied"})
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("detail", response.data)

    def test_drf_validation_error_with_detail_wrapper(self):
        """Test that DRF ValidationError gets wrapped in detail"""
        request = self.factory.get("/", {"exception_type": "drf_validation"})
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)
        self.assertIn("field", response.data["detail"])

    def test_unexpected_error_returns_none(self):
        """Test that unexpected errors return None (default Django handling)"""
        mock_ctx = {
            "view": TestExceptionHandlerView(),
            "request": self.factory.get("/"),
        }

        # Test with unexpected exception
        response = drf_default_with_modifications_exception_handler(
            Exception("Unexpected error"), mock_ctx
        )

        # Should return None for unexpected errors
        self.assertIsNone(response)

    def test_response_structure(self):
        """Test that all error responses have the expected structure"""
        test_cases = [
            ("django_validation", status.HTTP_400_BAD_REQUEST),
            ("http404", status.HTTP_404_NOT_FOUND),
            ("permission_denied", status.HTTP_403_FORBIDDEN),
            ("drf_validation", status.HTTP_400_BAD_REQUEST),
        ]

        for exception_type, expected_status in test_cases:
            with self.subTest(exception_type=exception_type):
                request = self.factory.get("/", {"exception_type": exception_type})
                response = self.view(request)

                self.assertEqual(response.status_code, expected_status)
                self.assertIn("detail", response.data)
                self.assertIsInstance(response.data, dict)

    def test_successful_request_still_works(self):
        """Test that normal successful requests still work"""
        request = self.factory.get("/")
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"success": True})

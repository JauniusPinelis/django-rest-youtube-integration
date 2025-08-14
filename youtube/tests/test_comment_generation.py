"""
Tests for CommentGenerationService.

Tests focus on AI comment generation, OpenAI integration, and mocking.
Following Django styleguide patterns for testing services.
"""

import os
from unittest.mock import Mock, patch
from django.test import TestCase
from django.core.exceptions import ValidationError
from openai import OpenAI
from ..models import Video, Comment
from ..services import CommentGenerationService


class CommentGenerationServiceTests(TestCase):
    """Test suite for CommentGenerationService business logic."""

    def setUp(self):
        """Set up test data and mock OpenAI client."""
        self.video = Video.objects.create(
            title="Test Video Tutorial",
            description="A comprehensive guide to testing",
            url="https://youtube.com/watch?v=test123",
        )

        # Create a mock OpenAI client
        self.mock_client = Mock(spec=OpenAI)
        self.service = CommentGenerationService(openai_client=self.mock_client)

    def test_init_with_provided_client_uses_that_client(self):
        """Test that initializing with a client uses the provided client."""
        mock_client = Mock(spec=OpenAI)
        service = CommentGenerationService(openai_client=mock_client)

        self.assertEqual(service.client, mock_client)

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-api-key"})
    @patch("youtube.services.OpenAI")
    def test_init_without_client_creates_new_client_with_api_key(
        self, mock_openai_class
    ):
        """Test that initializing without client creates new OpenAI client."""
        mock_client_instance = Mock()
        mock_openai_class.return_value = mock_client_instance

        service = CommentGenerationService()

        mock_openai_class.assert_called_once_with(api_key="test-api-key")
        self.assertEqual(service.client, mock_client_instance)

    @patch.dict(os.environ, {}, clear=True)
    def test_init_without_client_and_no_api_key_raises_validation_error(self):
        """Test that initializing without client and no API key raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            CommentGenerationService()

        self.assertEqual(
            str(cm.exception), "['OPENAI_API_KEY environment variable is required']"
        )

    def test_generate_comment_with_valid_response_returns_comment_text(self):
        """Test that generate_comment with valid OpenAI response returns comment text."""
        # Mock the OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Great tutorial! Very helpful."

        self.mock_client.chat.completions.create.return_value = mock_response

        result = self.service.generate_comment(
            video_title="Python Tutorial", video_description="Learn Python basics"
        )

        self.assertEqual(result, "Great tutorial! Very helpful.")

        # Verify the API was called with correct parameters
        self.mock_client.chat.completions.create.assert_called_once()
        call_args = self.mock_client.chat.completions.create.call_args

        self.assertEqual(call_args.kwargs["model"], "gpt-3.5-turbo")
        self.assertEqual(call_args.kwargs["max_tokens"], 100)
        self.assertEqual(call_args.kwargs["temperature"], 0.8)

        messages = call_args.kwargs["messages"]
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["role"], "user")
        self.assertIn("Python Tutorial", messages[1]["content"])

    def test_generate_comment_with_different_tones_includes_tone_in_prompt(self):
        """Test that different tones are included in the user prompt."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Excited comment!"

        self.mock_client.chat.completions.create.return_value = mock_response

        self.service.generate_comment(video_title="Amazing Video", tone="excited")

        call_args = self.mock_client.chat.completions.create.call_args
        user_message = call_args.kwargs["messages"][1]["content"]
        self.assertIn("excited", user_message)

    def test_generate_comment_includes_description_when_provided(self):
        """Test that video description is included in prompt when provided."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Good explanation!"

        self.mock_client.chat.completions.create.return_value = mock_response

        self.service.generate_comment(
            video_title="Tutorial",
            video_description="This is a detailed tutorial about programming",
        )

        call_args = self.mock_client.chat.completions.create.call_args
        user_message = call_args.kwargs["messages"][1]["content"]
        self.assertIn("This is a detailed tutorial", user_message)

    def test_generate_comment_truncates_long_descriptions(self):
        """Test that very long descriptions are truncated to 200 characters."""
        long_description = "A" * 300  # 300 characters

        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Nice video!"

        self.mock_client.chat.completions.create.return_value = mock_response

        self.service.generate_comment(
            video_title="Tutorial", video_description=long_description
        )

        call_args = self.mock_client.chat.completions.create.call_args
        user_message = call_args.kwargs["messages"][1]["content"]
        # Should contain only first 200 characters of description
        self.assertIn("A" * 200, user_message)
        self.assertNotIn("A" * 201, user_message)

    def test_generate_comment_with_empty_response_raises_validation_error(self):
        """Test that empty OpenAI response raises ValidationError."""
        mock_response = Mock()
        mock_response.choices = []

        self.mock_client.chat.completions.create.return_value = mock_response

        with self.assertRaises(ValidationError) as cm:
            self.service.generate_comment(video_title="Test Video")

        self.assertEqual(str(cm.exception), "['OpenAI API returned empty response']")

    def test_generate_comment_with_none_content_raises_validation_error(self):
        """Test that None content in response raises ValidationError."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = None

        self.mock_client.chat.completions.create.return_value = mock_response

        with self.assertRaises(ValidationError) as cm:
            self.service.generate_comment(video_title="Test Video")

        self.assertEqual(str(cm.exception), "['OpenAI API returned empty response']")

    def test_generate_comment_with_api_exception_raises_validation_error(self):
        """Test that OpenAI API exceptions are wrapped in ValidationError."""
        self.mock_client.chat.completions.create.side_effect = Exception("API Error")

        with self.assertRaises(ValidationError) as cm:
            self.service.generate_comment(video_title="Test Video")

        self.assertIn("Failed to generate comment", str(cm.exception))
        self.assertIn("API Error", str(cm.exception))

    def test_generate_comments_bulk_returns_multiple_comments(self):
        """Test that bulk generation returns correct number of comments."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Generated comment"

        self.mock_client.chat.completions.create.return_value = mock_response

        result = self.service.generate_comments_bulk(video_title="Test Video", count=3)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "Generated comment")
        self.assertEqual(result[1], "Generated comment")
        self.assertEqual(result[2], "Generated comment")

        # Should have made 3 API calls
        self.assertEqual(self.mock_client.chat.completions.create.call_count, 3)

    def test_generate_comments_bulk_with_custom_tones_uses_provided_tones(self):
        """Test that bulk generation with custom tones uses those tones."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Comment"

        self.mock_client.chat.completions.create.return_value = mock_response

        custom_tones = ["critical", "analytical"]

        self.service.generate_comments_bulk(
            video_title="Test Video", count=2, tones=custom_tones
        )

        # Check that the correct tones were used in the calls
        calls = self.mock_client.chat.completions.create.call_args_list

        # First call should use "critical" tone
        first_user_message = calls[0].kwargs["messages"][1]["content"]
        self.assertIn("critical", first_user_message)

        # Second call should use "analytical" tone
        second_user_message = calls[1].kwargs["messages"][1]["content"]
        self.assertIn("analytical", second_user_message)

    def test_generate_comments_bulk_with_more_comments_than_tones_cycles_tones(self):
        """Test that bulk generation cycles through tones when more comments than tones."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Comment"

        self.mock_client.chat.completions.create.return_value = mock_response

        self.service.generate_comments_bulk(
            video_title="Test Video",
            count=3,
            tones=["happy", "sad"],  # Only 2 tones for 3 comments
        )

        calls = self.mock_client.chat.completions.create.call_args_list

        # Should cycle: happy, sad, happy
        self.assertIn("happy", calls[0].kwargs["messages"][1]["content"])
        self.assertIn("sad", calls[1].kwargs["messages"][1]["content"])
        self.assertIn("happy", calls[2].kwargs["messages"][1]["content"])

    def test_generate_comments_bulk_with_count_over_10_raises_validation_error(self):
        """Test that requesting more than 10 comments raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            self.service.generate_comments_bulk(video_title="Test Video", count=11)

        self.assertEqual(
            str(cm.exception), "['Cannot generate more than 10 comments at once']"
        )

    def test_generate_and_save_comment_creates_and_saves_comment(self):
        """Test that generate_and_save_comment creates and saves comment to database."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Generated comment for database"

        self.mock_client.chat.completions.create.return_value = mock_response

        result = self.service.generate_and_save_comment(video_id=self.video.id)

        # Should return a Comment instance
        self.assertIsInstance(result, Comment)
        self.assertEqual(result.video, self.video)
        self.assertEqual(result.author, "AI User")
        self.assertEqual(result.content, "Generated comment for database")

        # Should be saved to database
        self.assertEqual(Comment.objects.count(), 1)
        saved_comment = Comment.objects.first()
        self.assertEqual(saved_comment.content, "Generated comment for database")

    def test_generate_and_save_comment_with_custom_author_and_tone(self):
        """Test generate_and_save_comment with custom author and tone."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Critical analysis comment"

        self.mock_client.chat.completions.create.return_value = mock_response

        result = self.service.generate_and_save_comment(
            video_id=self.video.id, author="Custom Author", tone="critical"
        )

        self.assertEqual(result.author, "Custom Author")

        # Check that the OpenAI call used critical tone
        call_args = self.mock_client.chat.completions.create.call_args
        user_message = call_args.kwargs["messages"][1]["content"]
        self.assertIn("critical", user_message)

    def test_generate_and_save_comment_with_nonexistent_video_raises_validation_error(
        self,
    ):
        """Test that generate_and_save_comment with non-existent video raises ValidationError."""
        with self.assertRaises(ValidationError) as cm:
            self.service.generate_and_save_comment(video_id=999)

        self.assertEqual(str(cm.exception), "['Video not found.']")

    def test_generate_and_save_comment_uses_video_title_and_description(self):
        """Test that generate_and_save_comment uses the video's title and description."""
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Comment about the tutorial"

        self.mock_client.chat.completions.create.return_value = mock_response

        self.service.generate_and_save_comment(video_id=self.video.id)

        # Check that the API call included video title and description
        call_args = self.mock_client.chat.completions.create.call_args
        user_message = call_args.kwargs["messages"][1]["content"]
        self.assertIn("Test Video Tutorial", user_message)
        self.assertIn("comprehensive guide to testing", user_message)

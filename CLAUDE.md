# Django YouTube API Project

## Setup Instructions

### Prerequisites
- Python 3.8+
- uv package manager


### Automated Test Suite
The project includes comprehensive automated tests organized following Django best practices:

#### Test Structure
```
youtube/tests/
├── __init__.py
├── test_services.py                # Service layer tests (business logic)
├── test_comment_generation.py      # AI comment generation service tests
├── test_api_videos.py              # Integration tests for video endpoints
├── test_api_comments.py            # Integration tests for comment endpoints
└── test_api_general.py             # General API tests (pagination, errors)
```

#### Test Categories
- **Service Layer Tests** (`test_services.py`): Business logic validation, service behavior, transaction handling
- **AI Comment Generation Tests** (`test_comment_generation.py`): OpenAI integration, mocking, comment generation logic
- **API Integration Tests** (`test_api_*.py`): HTTP requests/responses, serialization, endpoint behavior
- **Cross-cutting Tests** (`test_api_general.py`): Pagination, error handling, API consistency

#### Running Tests
```bash
# Run all tests
uv run python manage.py test

# Run specific test module
uv run python manage.py test youtube.tests.test_services
uv run python manage.py test youtube.tests.test_comment_generation
uv run python manage.py test youtube.tests.test_api_videos

# Run with verbose output
uv run python manage.py test -v 2

# Run specific test class
uv run python manage.py test youtube.tests.test_services.VideoServiceTests
```

### Test Coverage
- **65 focused test cases** following Django styleguide patterns
- **Service Layer Tests** (13 tests): Business logic, validation, error handling
- **AI Comment Generation Tests** (18 tests): OpenAI integration, mocking, comment generation
- **Video API Tests** (20 tests): CRUD operations, custom actions, edge cases
- **Comment API Tests** (11 tests): CRUD operations, filtering, validation
- **General API Tests** (3 tests): Pagination behavior, error handling

### Manual Testing with curl
```bash
# Get all videos
curl -X GET http://127.0.0.1:8000/api/videos/

# Create a video
curl -X POST http://127.0.0.1:8000/api/videos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Video", "description": "A test", "url": "https://youtube.com/test"}'

# Create a comment
curl -X POST http://127.0.0.1:8000/api/comments/ \
  -H "Content-Type: application/json" \
  -d '{"video": 1, "author": "User", "content": "Great video!"}'

# Increment views
curl -X POST http://127.0.0.1:8000/api/videos/1/increment_views/
```

### AI Comment Generation

The project includes an AI-powered comment generation service using OpenAI's API:

#### Prerequisites
- Set the `OPENAI_API_KEY` environment variable with your OpenAI API key:
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

#### Using the CommentGenerationService

```python
# Example usage in Django shell
from youtube.services import CommentGenerationService
from youtube.models import Video

# Initialize the service (will use OPENAI_API_KEY from environment)
service = CommentGenerationService()

# Generate a single comment
comment = service.generate_comment(
    video_title="Python Tutorial",
    video_description="Learn Python basics",
    tone="friendly"
)
print(comment)  # "Great tutorial! This really helped me understand Python basics."

# Generate multiple comments with different tones
comments = service.generate_comments_bulk(
    video_title="Django Tutorial",
    count=3,
    tones=["excited", "thoughtful", "appreciative"]
)

# Generate and save a comment directly to the database
video = Video.objects.first()
saved_comment = service.generate_and_save_comment(
    video_id=video.id,
    author="AI Assistant",
    tone="helpful"
)
```

#### Available Tones
- `friendly` - Casual, approachable comments
- `excited` - Enthusiastic, energetic comments  
- `thoughtful` - Analytical, reflective comments
- `appreciative` - Grateful, thankful comments
- `curious` - Question-asking, inquisitive comments
- `critical` - Constructive feedback comments

#### Service Features
- **Smart prompting**: Uses video title and description for context-aware comments
- **Bulk generation**: Generate up to 10 comments at once with varied tones
- **Database integration**: Generate and save comments directly to the database
- **Error handling**: Proper validation and exception handling for API failures
- **Testable design**: Fully mocked in tests for reliable CI/CD


## Implementation Details

### Features Implemented
- ✅ Django REST Framework setup with pagination
- ✅ Video model with all required fields
- ✅ Comment model with foreign key to Video
- ✅ Full CRUD operations for both models
- ✅ Custom actions (increment views, likes)
- ✅ Admin interface with search/filtering
- ✅ API filtering (comments by video)
- ✅ Service layer for business logic separation
- ✅ **AI Comment Generation** - OpenAI-powered comment generation with multiple tones
- ✅ **Celery Integration** - Background task processing and scheduled content generation
- ✅ Proper serializers with nested data
- ✅ Comprehensive automated test suite (65 focused tests following Django best practices)
- ✅ Input validation and error handling
- ✅ API documentation and examples

### Key Files
- `youtube/models.py` - Video and Comment models
- `youtube/services.py` - Business logic layer including AI comment generation service
- `youtube/tasks.py` - Celery tasks for scheduled content generation
- `youtube/serializers.py` - DRF serializers
- `youtube/views.py` - ViewSets with custom actions
- `youtube/urls.py` - API URL routing
- `youtube/admin.py` - Admin interface configuration
- `youtube/management/commands/setup_periodic_tasks.py` - Command to initialize scheduled tasks
- `youtube/tests/` - Comprehensive test suite following Django best practices
  - `test_comment_generation.py` - AI comment generation service tests (18 tests)
- `youtube_api/settings.py` - Django settings with DRF and Celery config
- `youtube_api/celery.py` - Celery application configuration
```json
{
    "id": 1,
    "title": "Sample Video",
    "description": "A sample video",
    "url": "https://youtube.com/watch?v=sample",
    "thumbnail_url": "https://img.youtube.com/vi/sample/maxresdefault.jpg",
    "duration": 300,
    "view_count": 1000,
    "like_count": 50,
    "created_at": "2025-08-10T07:00:00Z",
    "updated_at": "2025-08-10T07:00:00Z",
    "comments_count": 1,
    "comments": [
        {
            "id": 1,
            "author": "John Doe",
            "content": "Great video!",
            "like_count": 2,
            "created_at": "2025-08-10T07:05:00Z",
            "updated_at": "2025-08-10T07:05:00Z"
        }
    ]
}
```

## Celery Configuration (Scheduled Content Generation)

The project includes Celery for background task processing and scheduled content generation.

### Prerequisites for Celery
- Redis server (included in Docker setup)
- Set `OPENAI_API_KEY` environment variable for AI comment generation

### Celery Services
The system includes these scheduled tasks:
- **Video Generation**: Creates new videos every 30 minutes
- **User Engagement Simulation**: Adds views, likes, comments every 5 minutes
- **Statistics Generation**: Creates engagement reports every hour
- **Data Cleanup**: Removes old test data daily at 2 AM (optional)

### Setup Periodic Tasks
After setting up the project, initialize the scheduled tasks:
```bash
uv run python manage.py setup_periodic_tasks
```

### Manual Celery Commands (Development)
```bash
# Install dependencies first
uv sync

# Start Redis (if not using Docker)
# Install Redis locally or use: docker run -d -p 6379:6379 redis:7-alpine

# Run database migrations for Celery Beat
uv run python manage.py migrate django_celery_beat

# Start Celery worker
uv run celery -A youtube_api worker -l info

# Start Celery Beat scheduler (in another terminal)
uv run celery -A youtube_api beat -l info

# Monitor tasks (optional - install flower: pip install flower)
uv run celery -A youtube_api flower
```

### Docker Setup with Celery
The Docker Compose configuration includes all Celery services:
```bash
# Start all services (Django, PostgreSQL, Redis, Celery worker, Celery beat)
docker-compose up -d

# Setup periodic tasks in Docker
docker-compose exec web uv run python manage.py setup_periodic_tasks

# View logs
docker-compose logs -f celery_worker
docker-compose logs -f celery_beat
```

### Available Celery Tasks
- `youtube.tasks.generate_video_content` - Creates new videos with AI-generated content
- `youtube.tasks.generate_comments_for_video` - Generates AI comments for a specific video
- `youtube.tasks.simulate_user_engagement` - Simulates views, likes, and user activity
- `youtube.tasks.generate_engagement_stats` - Creates analytics and statistics
- `youtube.tasks.cleanup_old_data` - Removes old test data to prevent database bloat

### Manual Task Execution
```bash
# Django shell examples
uv run python manage.py shell

# Generate a single video
from youtube.tasks import generate_video_content
result = generate_video_content.delay()
print(result.get())

# Generate comments for video ID 1
from youtube.tasks import generate_comments_for_video  
result = generate_comments_for_video.delay(1, 3)
print(result.get())

# Simulate user engagement
from youtube.tasks import simulate_user_engagement
result = simulate_user_engagement.delay()
print(result.get())
```

## Development Commands
- Start server: `uv run python manage.py runserver`
- Make migrations: `uv run python manage.py makemigrations`
- Apply migrations: `uv run python manage.py migrate`
- Create superuser: `uv run python manage.py createsuperuser`
- Django shell: `uv run python manage.py shell`
- Run tests: `uv run python manage.py test`

## Admin Interface
Access the admin interface at `http://127.0.0.1:8000/admin/` to manage videos and comments through Django's built-in admin panel.

## Commit Guidelines
- Use short, concise commit messages
- Do NOT include "Generated by Claude" or similar footers
- Focus on what was changed, not how it was done
- Examples: "Add video model", "Fix API pagination", "Update README"

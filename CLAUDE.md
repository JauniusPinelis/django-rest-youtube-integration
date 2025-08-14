# Django YouTube API Project

## Prerequisites
- Python 3.8+
- uv package manager
- Redis for Celery
- OpenAI API key for comment generation

## Development Commands
- Start server: `uv run python manage.py runserver`
- Run tests: `uv run python manage.py test`
- Make migrations: `uv run python manage.py makemigrations`
- Apply migrations: `uv run python manage.py migrate`
- Create superuser: `uv run python manage.py createsuperuser`

## Features
- Django REST Framework with pagination
- Video and Comment models with full CRUD
- AI comment generation with OpenAI
- Celery background tasks and scheduling
- Admin interface with search/filtering
- Comprehensive test suite (65 tests)

## Key Files
- `youtube/models.py` - Data models
- `youtube/services.py` - Business logic and AI services
- `youtube/tasks.py` - Celery background tasks
- `youtube/views.py` - API endpoints
- `youtube/tests/` - Test suite

## API Usage
```bash
# Get videos
curl http://127.0.0.1:8000/api/videos/

# Create video
curl -X POST http://127.0.0.1:8000/api/videos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "url": "https://youtube.com/test"}'

# Create comment
curl -X POST http://127.0.0.1:8000/api/comments/ \
  -H "Content-Type: application/json" \
  -d '{"video": 1, "author": "User", "content": "Great!"}'
```

## AI Comment Generation
```python
from youtube.services import CommentGenerationService

service = CommentGenerationService()
comment = service.generate_comment(
    video_title="Tutorial",
    video_description="Learn basics",
    tone="friendly"
)
```

## Celery Setup
```bash
# Setup
uv run python manage.py setup_periodic_tasks

# Start worker and scheduler
uv run celery -A youtube_api worker -l info
uv run celery -A youtube_api beat -l info
```

## Docker
```bash
docker-compose up -d
docker-compose exec web uv run python manage.py setup_periodic_tasks
```

## Testing
```bash
uv run python manage.py test
uv run python manage.py test youtube.tests.test_services
```

## Code Guidelines
- Follow Django conventions
- Use existing patterns and libraries
- Keep commit messages concise

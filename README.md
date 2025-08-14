# Django YouTube Integration Simulation

A Django REST API simulating YouTube video and comment management with AI-generated comments and background task processing.

## Setup & Run

### Prerequisites
- Python 3.8+
- uv package manager
- Redis (for Celery)
- OpenAI API key (optional, for comment generation)

### Quick Start

1. **Install dependencies**
   ```bash
   uv sync
   ```

2. **Setup environment**
   ```bash
   cp .env.example .env  # Add your OpenAI API key
   ```

3. **Run migrations**
   ```bash
   uv run python manage.py migrate
   ```

4. **Start the server**
   ```bash
   uv run python manage.py runserver
   ```

5. **Create admin user (optional)**
   ```bash
   uv run python manage.py createsuperuser
   ```

### Using Docker (Preferred)
```bash
docker-compose up -d
docker-compose exec web uv run python manage.py migrate
docker-compose exec web uv run python manage.py createsuperuser
```

## Features

- **CRUD Operations**: Full video and comment management
- **AI Comment Generation**: OpenAI-powered comment creation
- **Background Tasks**: Celery-based content population
- **Admin Interface**: Django admin with search/filtering
- **REST API**: Paginated endpoints with engagement stats
- **Comprehensive Tests**: 65+ test cases

## API Endpoints

- `GET /api/videos/` - List videos with pagination
- `POST /api/videos/` - Create new video  
- `GET /api/videos/{id}/` - Video details with comments
- `POST /api/videos/{id}/like/` - Like/unlike video
- `POST /api/videos/{id}/increment_views/` - Increment view count
- `GET /api/comments/` - List comments
- `POST /api/comments/` - Create comment

## Testing

```bash
uv run python manage.py test
```

## Development Journey

This project was built as a technical assessment with focus on Django best practices and rapid feature delivery.

**Task Interpretation:**
The task was somewhat abstract, so I interpreted it as building a complete CRUD system for YouTube videos and comments with additional engagement functionality. The goal was to simulate a YouTube integration without actual API calls.

**Development Approach & Tooling:**
- **AI-Assisted Development**: Most code was generated using Claude Code, which enabled rapid feature delivery within the 6-8 hour time constraint. While this may not optimize for minimalism, it allowed comprehensive feature coverage and extensive testing.
- **Documentation Strategy**: Downloaded relevant Django/DRF docs to `/docs` folder and referenced them during Claude Code sessions (preferred over Context7 MCP for better control).
- **Modern Python Stack**: Employed uv for package management, ruff for linting, mypy for type checking, and pre-commit hooks for quality assurance.

**Architecture Decisions:**
- **Service-Based Architecture**: Separated business logic from views following [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide) principles for maintainability and testability.
- **One Class Per File**: Maintained logical file structure for better organization.
- **Familiar Patterns**: Applied Django concepts from previous projects including logical folder structure and service layers.

**Implementation Details:**
- **Celery Integration**: Implemented Celery Beat for scheduled content population with task logging to PostgreSQL.
- **AI Comment Generation**: Used OpenAI's structured mode for realistic comment generation.
- **Testing Strategy**: Comprehensive test suite covering both API endpoints and service logic (65+ tests).
- **Admin Interface**: Enhanced Django admin with search/filtering capabilities.
- **Quality Assurance**: Pre-commit hooks ensure formatting standards and test passage.

**Technical Decisions Justified:**
- **Docker Setup**: Provides consistent environment and handles dependencies (Redis, PostgreSQL).
- **PostgreSQL**: Chosen over SQLite for production-ready features and Celery task logging.
- **Service Layer**: Keeps views thin and business logic testable independently.

**Time Investment:** 6-8 hours focused on feature completeness and test coverage over code optimization.

**Given More Time, I Would:**
- **Code Review**: Thorough review of generated code, removing unnecessary try/catch blocks, modernizing type hints (use `str | None` instead of `Optional[str]`).
- **Manual Testing**: Extended manual testing to ensure all edge cases work as expected.
- **Test Reliability**: Review and strengthen test suite to ensure trustworthy coverage.
- **Deployment**: Deploy to AWS with RabbitMQ for Celery instead of Redis.
- **Performance**: Add monitoring, logging, and performance optimizations.

Admin credentials: `admin/admin`
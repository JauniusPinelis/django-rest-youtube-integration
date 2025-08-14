# Django YouTube API

A Django REST API for managing YouTube videos and comments.

## Quick Start

### Prerequisites
- Python 3.8+
- uv package manager

### Setup & Run

1. **Install dependencies**
   ```bash
   uv add Django djangorestframework requests
   ```

2. **Run migrations**
   ```bash
   uv run python manage.py migrate
   ```

3. **Start the server**
   ```bash
   uv run python manage.py runserver
   ```

4. **Access the API**
   - API: http://127.0.0.1:8000/api/videos/
   - Admin: http://127.0.0.1:8000/admin/ (create superuser first)

### Create Admin User (Optional)
```bash
uv run python manage.py createsuperuser
```

### Test the API
```bash
uv run python test_api.py
```

## API Endpoints

- `GET /api/videos/` - List videos
- `POST /api/videos/` - Create video
- `GET /api/videos/{id}/` - Video details with comments
- `POST /api/videos/{id}/increment_views/` - Increment views
- `POST /api/videos/{id}/like/` - Like video
- `GET /api/comments/` - List comments
- `POST /api/comments/` - Create comment

See CLAUDE.md for detailed documentation.

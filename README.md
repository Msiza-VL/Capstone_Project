# Fitness Tracker API

A RESTful API for tracking fitness activities built with Django and Django REST Framework.

## Features

- User authentication with JWT
- CRUD operations for fitness activities
- Activity history and metrics
- Filtering and pagination
- User-specific data access

## Setup

1. Clone the repository:
bash
git clone <repository-url>
cd fitness_tracker_api

2. Create and activate virtual environment:
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
bash
pip install -r requirements.txt

4. Create .env file and set environment variables:

SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

bash
python manage.py makemigrations
python manage.py migrate
6. Create superuser:
bash
python manage.py createsuperuser
7. Run the development server:
bash
python manage.py runserver
## API Endpoints

- POST /api/auth/register/ - Register new user
- POST /api/auth/token/ - Get JWT token
- POST /api/auth/token/refresh/ - Refresh JWT token
- GET /api/activities/ - List all activities
- POST /api/activities/ - Create new activity
- GET /api/activities/{id}/ - Retrieve activity
- PUT /api/activities/{id}/ - Update activity
- DELETE /api/activities/{id}/ - Delete activity
- GET /api/metrics/ - Get activity metrics
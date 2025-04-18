# Person API

A simple RESTful API built with Django Rest Framework to view person records, and simulates api consumption using Python requests library.

## Overview

This API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on person records. It allows you to:

- List all persons
- Create a new person
- Retrieve a specific person by ID
- Update a person's details
- Delete a person

## Technologies Used

- Django
- Django Rest Framework
- Python
- Python requests library for API testing

## Installation

1. Clone this repository
```bash
git clone https://github.com/Melchizedeke/myApi.git
cd myApi
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install django djangorestframework requests
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver 9090
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/persons/` | GET | Get all persons |
| `/api/persons/` | POST | Create a new person |
| `/api/persons/<id>/` | GET | Get a specific person |
| `/api/persons/<id>/` | PUT | Update a specific person |
| `/api/persons/<id>/` | DELETE | Delete a specific person |

## Usage Examples

### List all persons
```bash
curl -X GET http://localhost:8000/persons/
```

### Create a new person
```bash
curl -X POST http://localhost:8000/persons/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 30, "country":"Nigeria", "programming_language":"Python"}'
```

### Get a specific person
```bash
curl -X GET http://localhost:8000/persons/1/
```

### Update a person
```bash
curl -X PUT http://localhost:8000/persons/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Smith", "age": 35, "country":"France", "programming_language":"Python"}'
```

### Delete a person
```bash
curl -X DELETE http://localhost:8000/persons/1/
```

## Project Structure

```
myApi/
├── manage.py
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
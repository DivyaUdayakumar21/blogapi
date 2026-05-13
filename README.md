# 📝 Blog API

A RESTful Blog API built with **Django** and **Django REST Framework**, featuring authentication, OpenAPI documentation, and production-ready deployment via Gunicorn.

---

## 🌐 Live URLs

| | URL |
|---|---|
| 📚 Swagger Docs | [blogapi-1mga.onrender.com/api/docs/swagger/](https://blogapi-1mga.onrender.com/api/docs/swagger/) |
| 🔌 API Base URL | [blogapi-1mga.onrender.com/api/v1/](https://blogapi-1mga.onrender.com/api/v1/) |

---

## 🚀 Features

- Full CRUD operations for blog posts
- Token-based authentication via `dj-rest-auth`
- Auto-generated OpenAPI / Swagger documentation with `drf-spectacular`
- SQLite database (development) — easily swappable for PostgreSQL in production
- Production-ready with Gunicorn WSGI server

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6.0.4 |
| API | Django REST Framework 3.17.1 |
| Auth | dj-rest-auth 7.2.0 + django-allauth |
| API Docs | drf-spectacular 0.29.0 |
| Server | Gunicorn 23.0.0 |
| Database | SQLite (via Django ORM) |

---

## 📁 Project Structure

```
blogapi/
├── blog_project/        # Django project settings & URL config
├── posts/               # Blog posts app (models, views, serializers, URLs)
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/DivyaUdayakumar21/blogapi.git
cd blogapi

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (optional, for admin access)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## 📖 API Documentation

Interactive API docs are auto-generated via `drf-spectacular`:

| UI | URL |
|---|---|
| Swagger UI (Live) | [/api/docs/swagger/](https://blogapi-1mga.onrender.com/api/docs/swagger/) |
| API Base (Live) | [/api/v1/](https://blogapi-1mga.onrender.com/api/v1/) |
| Local Swagger | `http://127.0.0.1:8000/api/docs/swagger/` |

---

## 🔐 Authentication

This API uses token-based authentication powered by `dj-rest-auth`.

| Endpoint | Method | Description |
|---|---|---|
| `/auth/login/` | POST | Log in and receive a token |
| `/auth/logout/` | POST | Log out |
| `/auth/registration/` | POST | Register a new user |
| `/auth/password/change/` | POST | Change password |

Include the token in request headers:

```
Authorization: Token <your_token_here>
```

---

## 📬 Blog Post Endpoints

| Endpoint | Method | Description | Auth Required |
|---|---|---|---|
| `/posts/` | GET | List all posts | No |
| `/posts/` | POST | Create a new post | Yes |
| `/posts/<id>/` | GET | Retrieve a post | No |
| `/posts/<id>/` | PUT/PATCH | Update a post | Yes |
| `/posts/<id>/` | DELETE | Delete a post | Yes |

---

## 🚢 Deployment

This project uses **Gunicorn** as the production WSGI server.

```bash
gunicorn blog_project.wsgi:application --bind 0.0.0.0:8000
```

For production, also make sure to:

- Set `DEBUG = False` in settings
- Configure `ALLOWED_HOSTS`
- Use environment variables for `SECRET_KEY` and database credentials
- Switch to PostgreSQL for a production-grade database

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📄 License

This project is open source. Feel free to use and modify it.

---

## 👩‍💻 Author

**Divya Udayakumar**  
[GitHub](https://github.com/DivyaUdayakumar21)

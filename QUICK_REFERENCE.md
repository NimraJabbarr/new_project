# 🚀 School CRM - Quick Reference Guide

## 📂 Project Structure

```
school_crm_project/
├── .env                          # Environment variables (local)
├── .env.example                  # Template for env variables
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
├── pythonanywhere_wsgi.py         # WSGI config for PythonAnywhere
├── PYTHONANYWHERE_SETUP.md        # Detailed setup guide
├── DEPLOYMENT_CHECKLIST.md        # Pre-deployment checklist
│
├── myenv/                        # Virtual environment (local only)
│
└── school_crm/                   # Main Django project
    ├── manage.py
    ├── db.sqlite3               # Local database (not used in production)
    │
    ├── school_crm/              # Project settings
    │   ├── settings.py          # Django settings (uses .env)
    │   ├── urls.py              # Main URL router
    │   ├── wsgi.py              # WSGI application
    │   └── views.py
    │
    ├── accounts/                # User authentication app
    ├── students/                # Students management app
    ├── teachers/                # Teachers management app
    ├── classrooms/              # Classrooms management app
    ├── attendance/              # Attendance tracking app
    │
    ├── templates/               # HTML templates
    ├── staticfiles/             # Static files (CSS, JS, images)
    └── media/                   # User uploads (student/teacher photos)
```

---

## 🔌 Database Configuration

### Local Development
- **Engine**: PostgreSQL
- **Host**: `ep-morning-moon-apbbe5li-pooler.c-7.us-east-1.aws.neon.tech`
- **Database**: `neondb`
- **User**: `neondb_owner`
- **Port**: `5432`
- **SSL**: Required (`sslmode=require`)

### Connection Details
All credentials are stored in `.env` file:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=npg_u4FEOcbZd2fv
DB_HOST=ep-morning-moon-apbbe5li-pooler.c-7.us-east-1.aws.neon.tech
DB_PORT=5432
```

---

## 🔧 Common Commands

### Development Setup
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
myenv\Scripts\activate    # Windows
source myenv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Install additional package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### Database Management
```bash
# Apply migrations
python manage.py migrate

# Make migrations (after model changes)
python manage.py makemigrations

# Create superuser (admin)
python manage.py createsuperuser

# Access database shell
python manage.py dbshell

# Dump database data
python manage.py dumpdata > backup.json

# Load database data
python manage.py loaddata backup.json
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Remove and re-collect
python manage.py collectstatic --clear --noinput
```

### Running Server
```bash
# Development server (default: localhost:8000)
python manage.py runserver

# Run on specific port
python manage.py runserver 8001

# Make accessible from other machines
python manage.py runserver 0.0.0.0:8000
```

### Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts

# Run specific test file
python manage.py test accounts.tests
```

---

## 📡 API Endpoints

### Authentication
- `POST /api/token/` - Get JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### User Management
- `POST /api/register/` - Register new user
- `POST /api/login/` - Login user
- `GET /api/profile/` - Get user profile (authenticated)
- `POST /api/profile/` - Update profile (authenticated)
- `POST /api/logout/` - Logout user (authenticated)

### Students
- `GET /api/students/` - List all students
- `GET /api/students/{id}/` - Get student details
- `POST /api/students/` - Create student
- `PUT /api/students/{id}/` - Update student
- `DELETE /api/students/{id}/` - Delete student

### Teachers
- `GET /api/teachers/` - List all teachers
- `GET /api/teachers/{id}/` - Get teacher details
- `POST /api/teachers/` - Create teacher
- `PUT /api/teachers/{id}/` - Update teacher
- `DELETE /api/teachers/{id}/` - Delete teacher

### Classrooms
- `GET /api/classrooms/` - List all classrooms
- `GET /api/classrooms/{id}/` - Get classroom details
- `POST /api/classrooms/` - Create classroom
- `PUT /api/classrooms/{id}/` - Update classroom
- `DELETE /api/classrooms/{id}/` - Delete classroom

### Attendance
- `GET /api/attendance/` - List all attendance records
- `POST /api/attendance/` - Create attendance record
- `PUT /api/attendance/{id}/` - Update attendance record
- `DELETE /api/attendance/{id}/` - Delete attendance record

---

## 🔐 Environment Variables

### Required for Production
```
SECRET_KEY=your-secure-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.pythonanywhere.com

DB_ENGINE=django.db.backends.postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=your-neon-password
DB_HOST=your-neon-host
DB_PORT=5432
```

### For Development
```
SECRET_KEY=django-insecure-development-key
DEBUG=True
ALLOWED_HOSTS=*
```

---

## 🐛 Debugging

### Enable Debug Mode
```python
# In settings.py (not recommended for production)
DEBUG = True
```

### Check Configuration
```bash
python manage.py check
```

### View Raw SQL Queries
```python
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as ctx:
    # Your code here
    pass

for query in ctx.captured_queries:
    print(query['sql'])
```

---

## 📝 Useful Files to Know

| File | Purpose |
|------|---------|
| `settings.py` | Django configuration |
| `urls.py` | URL routing |
| `models.py` | Database models |
| `serializers.py` | DRF serializers |
| `views.py` | API views/logic |
| `admin.py` | Admin panel configuration |
| `manage.py` | Django CLI tool |

---

## ⚠️ Important Notes

1. **Never commit `.env` file** - It contains sensitive credentials
2. **Always use HTTPS** - PythonAnywhere provides free HTTPS
3. **Database backups** - Regularly backup your Neon database
4. **Static files** - Run `collectstatic` after deploying changes
5. **Migrations** - Always run migrations in order
6. **Superuser** - Create admin account before going live

---

## 🔗 Useful Links

- [Django Documentation](https://docs.djangoproject.com/en/6.0/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PythonAnywhere Help](https://www.pythonanywhere.com/help/)
- [Neon PostgreSQL](https://neon.tech/docs/)
- [JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)

---

## 📞 Troubleshooting Quick Links

- [500 Errors](./DEPLOYMENT_CHECKLIST.md#-troubleshooting)
- [Database Issues](./PYTHONANYWHERE_SETUP.md#-troubleshooting)
- [Deployment Errors](./DEPLOYMENT_CHECKLIST.md#-post-deployment-testing)

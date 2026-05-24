# 📋 Deployment Checklist for School CRM

## ✅ Local Development (Completed)

- [x] Django project connected to Neon PostgreSQL
- [x] Environment variables configured in `.env` file
- [x] All migrations applied to database
- [x] Virtual environment set up with all dependencies
- [x] Static files collected
- [x] Server running successfully on `http://localhost:8000/`
- [x] Database connection tested and verified

---

## 🚀 Before Deploying to PythonAnywhere

### Security Checklist

- [ ] Generate a new `SECRET_KEY` for production:

  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```

- [ ] Set `DEBUG=False` in `.env`
- [ ] Update `ALLOWED_HOSTS` to include your PythonAnywhere domain
- [ ] Ensure `.env` file is in `.gitignore` (✅ Already done)
- [ ] Verify Neon SSL certificate is trusted
- [ ] Create a strong password for Neon database if needed

### Project Preparation

- [ ] Update `requirements.txt`: `pip freeze > requirements.txt`
- [ ] Test locally one more time: `python manage.py runserver`
- [ ] Run migrations locally: `python manage.py migrate`
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Create superuser for admin panel: `python manage.py createsuperuser`

### Credentials to Have Ready

- [ ] PythonAnywhere username
- [ ] PythonAnywhere password
- [ ] Neon database connection string
  - Host: `ep-morning-moon-apbbe5li-pooler.c-7.us-east-1.aws.neon.tech`
  - Database: `neondb`
  - User: `neondb_owner`
  - Password: (securely stored)
- [ ] New `SECRET_KEY` for production

---

## 🔧 Step-by-Step PythonAnywhere Setup

### 1. Initial Setup
- [ ] Log in to PythonAnywhere
- [ ] Open a **Bash console**
- [ ] Clone your repository OR upload your project
  ```bash
  cd ~
  git clone https://github.com/yourusername/school-crm.git school_crm_project
  # OR
  # Upload and extract your project to ~/school_crm_project
  ```

### 2. Virtual Environment

- [ ] Create virtual environment:

  ```bash
  cd ~/school_crm_project
  mkvirtualenv --python=/usr/bin/python3.11 school_crm_env
  ```

- [ ] Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 3. Static Files & Media
- [ ] Collect static files:

  ```bash
  cd ~/school_crm_project/school_crm
  python manage.py collectstatic --noinput
  ```

### 4. Web App Configuration

- [ ] Go to **Web** tab → **Add a new web app**
- [ ] Select **Manual configuration** → Python 3.11
- [ ] Copy WSGI configuration from `pythonanywhere_wsgi.py`
- [ ] Update the WSGI file in PythonAnywhere settings with proper paths
- [ ] Set virtualenv path: `/home/yourusername/.virtualenvs/school_crm_env`

### 5. Static Files Mapping

- [ ] URL: `/static/` → Directory: `/home/yourusername/school_crm_project/school_crm/staticfiles`
- [ ] URL: `/media/` → Directory: `/home/yourusername/school_crm_project/school_crm/media`

### 6. Environment Setup
- [ ] Create `.env` file in `/home/yourusername/school_crm_project/`
- [ ] Add all environment variables (copy from local `.env`)
- [ ] **Important**: Use production credentials and strong `SECRET_KEY`

### 7. Database Migrations
- [ ] In Bash console:
  ```bash
  cd ~/school_crm_project/school_crm
  source ~/.virtualenvs/school_crm_env/bin/activate
  python manage.py migrate
  python manage.py createsuperuser  # Create admin user
  ```

### 8. Deploy
- [ ] Click **Reload** button in Web tab
- [ ] Wait for 30 seconds for changes to take effect

---

## 🧪 Post-Deployment Testing

- [ ] Visit `https://yourusername.pythonanywhere.com/` → Should see homepage
- [ ] Visit `https://yourusername.pythonanywhere.com/admin/` → Should see login
- [ ] Login with superuser credentials created earlier
- [ ] Test API: `https://yourusername.pythonanywhere.com/api/students/` (should return 401 Unauthorized without auth)
- [ ] Check PythonAnywhere error log if anything fails

---

## 🔐 Environment Variables for Production (.env)

```
SECRET_KEY=<generate-new-strong-key>
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=<your-neon-password>
DB_HOST=ep-morning-moon-apbbe5li-pooler.c-7.us-east-1.aws.neon.tech
DB_PORT=5432
```

---

## 🆘 Troubleshooting

### 500 Error
1. Check error log in PythonAnywhere Web tab
2. Verify `.env` file exists and is readable
3. Verify Neon credentials are correct
4. Check migrations were applied

### ModuleNotFoundError
1. Verify virtual environment path in Web tab
2. Reinstall requirements: `pip install -r requirements.txt`

### Static Files Not Loading
1. Re-run: `python manage.py collectstatic --noinput`
2. Verify paths in Static files section match exactly

### Database Connection Failed
1. Test connection from Bash: `python manage.py dbshell`
2. Verify `.env` has correct Neon credentials
3. Check if Neon project is active

---

## 📞 Support

- **PythonAnywhere Help**: https://www.pythonanywhere.com/help/
- **Django Docs**: https://docs.djangoproject.com/en/6.0/
- **Neon Docs**: https://neon.tech/docs/

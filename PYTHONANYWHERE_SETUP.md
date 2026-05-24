# 🚀 PythonAnywhere Deployment Guide for School CRM

## Step 1: Prepare Your Project for PythonAnywhere

### 1.1 Create .env File with Your Credentials
Before uploading to PythonAnywhere, ensure you have a `.env` file in the root directory with:

```
SECRET_KEY=your-django-secret-key
DB_ENGINE=django.db.backends.postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=npg_u4FEOcbZd2fv
DB_HOST=ep-morning-moon-apbbe5li-pooler.c-7.us-east-1.aws.neon.tech
DB_PORT=5432
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,schoolcrm786.pythonanywhere.com
```

### 1.2 Update requirements.txt
Run: `pip freeze > requirements.txt`

---

## Step 2: Upload Project to PythonAnywhere

### 2.1 Using Git (Recommended)
```bash
cd ~
git clone https://github.com/yourusername/school-crm.git school_crm_project
cd school_crm_project
```

### 2.2 Using Manual Upload
- Zip your project (excluding `__pycache__`, `.git`, `myenv/`)
- Upload via PythonAnywhere Web Interface
- Extract to `/home/yourusername/school_crm_project`

---

## Step 3: Set Up Virtual Environment on PythonAnywhere

Open a **Bash console** on PythonAnywhere:

```bash
cd ~/school_crm_project
mkvirtualenv --python=/usr/bin/python3.11 school_crm_env
pip install -r requirements.txt
```

---

## Step 4: Collect Static Files

```bash
cd ~/school_crm_project/school_crm
python manage.py collectstatic --noinput
```

---

## Step 5: Create Web App on PythonAnywhere

1. Go to **Web** tab → Click **Add a new web app**
2. Choose **Manual configuration** → Python 3.11
3. Edit the WSGI configuration file with this content:

```python
import os
import sys

project_folder = os.path.expanduser('~/school_crm_project')
sys.path.insert(0, project_folder)
sys.path.insert(0, os.path.join(project_folder, 'school_crm'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'school_crm.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

---

## Step 6: Configure Virtual Environment in Web App

In **Web** tab:
- **Virtualenv path**: `/home/yourusername/.virtualenvs/school_crm_env`

---

## Step 7: Configure Static Files

In **Web** tab → **Static files**:

Add mapping:
```
URL: /static/
Directory: /home/yourusername/school_crm_project/school_crm/staticfiles
```

Add mapping:
```
URL: /media/
Directory: /home/yourusername/school_crm_project/school_crm/media
```

---

## Step 8: Add Environment Variables

1. Create `.env` file in `/home/yourusername/school_crm_project/`
2. Add all your environment variables (as shown in Step 1)

**Important**: Ensure the `.env` file is in the project root (same level as `requirements.txt`)

---

## Step 9: Run Migrations on PythonAnywhere

Open **Bash console**:

```bash
cd ~/school_crm_project/school_crm
source ~/.virtualenvs/school_crm_env/bin/activate
python manage.py migrate
```

---

## Step 10: Reload Web App

Click **Reload** in the **Web** tab

---

## 🔒 Security Checklist

- ✅ Set `DEBUG = False` in `.env`
- ✅ Update `SECRET_KEY` to a strong random value
- ✅ Ensure `.env` is in `.gitignore`
- ✅ Update `ALLOWED_HOSTS` with your PythonAnywhere domain
- ✅ Use HTTPS (enabled by default on PythonAnywhere)
- ✅ Check database SSL settings for Neon

---

## 📝 Testing

After deployment:
1. Visit `https://yourusername.pythonanywhere.com/`
2. Test API endpoints: `https://yourusername.pythonanywhere.com/api/students/`
3. Access admin: `https://yourusername.pythonanywhere.com/admin/`

---

## ❌ Troubleshooting

### Issue: ModuleNotFoundError
- **Solution**: Ensure virtual environment path is correct in Web tab

### Issue: 500 Error
- **Solution**: Check error log in **Web** tab → Scroll to error log files

### Issue: Database Connection Failed
- **Solution**: Verify `.env` file exists and Neon credentials are correct

### Issue: Static Files Not Loading
- **Solution**: Run `python manage.py collectstatic --noinput` again

---

## 🔗 Useful Links

- PythonAnywhere Web Help: https://www.pythonanywhere.com/help/
- Django Deployment: https://docs.djangoproject.com/en/6.0/howto/deployment/
- Neon Documentation: https://neon.tech/docs/

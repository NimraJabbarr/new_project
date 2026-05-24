"""
WSGI config for school_crm project for PythonAnywhere.
It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys
from pathlib import Path

# ✅ Add your project directory to the sys.path
project_folder = os.path.expanduser('~/school_crm_project')
sys.path.insert(0, project_folder)
sys.path.insert(0, os.path.join(project_folder, 'school_crm'))

# ✅ Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'school_crm.settings'

# ✅ Setup Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

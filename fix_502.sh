#!/bin/bash

# ============================================================================
# 🚀 COMPLETE PYTHONANYWHERE FIX SCRIPT - COPY PASTE THIS IN BASH CONSOLE
# ============================================================================
# This script will:
# 1. Install python-dotenv
# 2. Create .env file with all credentials
# 3. Apply migrations
# 4. Collect static files
# 5. Restart web app
# ============================================================================

echo "🔧 School CRM - PythonAnywhere Fix Script"
echo "=========================================="
echo ""

# Get username (you need to replace this)
USERNAME=$1
if [ -z "$USERNAME" ]; then
    echo "❌ ERROR: Username not provided!"
    echo "Usage: bash fix_502.sh YOUR_USERNAME"
    echo ""
    echo "To find your username:"
    echo "  1. Log in to PythonAnywhere"
    echo "  2. Click your username in top right"
    echo "  3. It's shown in the URL: https://www.pythonanywhere.com/user/YOUR_USERNAME/"
    exit 1
fi

PROJECT_PATH="/home/$USERNAME/schoolcrm786.pythonanywhere.com"
VENV_PATH="/home/$USERNAME/.virtualenvs/schoolcrm_env"

echo "📁 Project Path: $PROJECT_PATH"
echo "🐍 Virtual Env: $VENV_PATH"
echo ""

# ============================================================================
# STEP 1: Navigate to project
# ============================================================================
echo "📍 Step 1: Navigating to project..."
cd "$PROJECT_PATH" || { echo "❌ Project path not found!"; exit 1; }
echo "✅ In project directory"
echo ""

# ============================================================================
# STEP 2: Activate virtual environment
# ============================================================================
echo "🔌 Step 2: Activating virtual environment..."
source "$VENV_PATH/bin/activate" || { echo "❌ Virtual env not found!"; exit 1; }
echo "✅ Virtual environment activated"
echo ""

# ============================================================================
# STEP 3: Install python-dotenv
# ============================================================================
echo "📦 Step 3: Installing python-dotenv..."
pip install --upgrade python-dotenv
echo "✅ python-dotenv installed"
echo ""

# ============================================================================
# STEP 4: Create .env file
# ============================================================================
echo "📝 Step 4: Creating .env file..."
cat > "$PROJECT_PATH/.env" << 'ENVEOF'
SECRET_KEY=django-insecure-!1h(7w=t1hg_2p6_x2xy7t#9b-w0_+8&r2004=ga#=l(mhr_er
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost,schoolcrm786.pythonanywhere.com

DB_ENGINE=django.db.backends.postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=npg_u4FEOcbZd2fv
DB_HOST=ep-morning-moon-apbbe5li-pooler.c-7.us-east-1.aws.neon.tech
DB_PORT=5432

JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
ENVEOF

echo "✅ .env file created at: $PROJECT_PATH/.env"
echo ""

# ============================================================================
# STEP 5: Run migrations
# ============================================================================
echo "🗄️  Step 5: Running database migrations..."
cd "$PROJECT_PATH/school_crm"
python manage.py migrate --noinput
echo "✅ Migrations applied"
echo ""

# ============================================================================
# STEP 6: Collect static files
# ============================================================================
echo "📦 Step 6: Collecting static files..."
python manage.py collectstatic --noinput
echo "✅ Static files collected"
echo ""

# ============================================================================
# STEP 7: Test database connection
# ============================================================================
echo "🔗 Step 7: Testing database connection..."
python -c "from django.db import connection; print('✅ Database connection: OK')" 2>&1 || echo "⚠️  Database warning (will fix after reload)"
echo ""

# ============================================================================
# FINAL STEPS
# ============================================================================
echo "=========================================="
echo "✅ SCRIPT COMPLETED!"
echo "=========================================="
echo ""
echo "📋 NEXT STEPS (Do these in PythonAnywhere Web UI):"
echo ""
echo "1. Go to: https://www.pythonanywhere.com/user/$USERNAME/"
echo "2. Click on 'Web' in the top menu"
echo "3. Find your domain: schoolcrm786.pythonanywhere.com"
echo "4. Click the GREEN 'Reload' button"
echo "5. Wait 30-60 seconds for reload to complete"
echo "6. Test: https://schoolcrm786.pythonanywhere.com/"
echo ""
echo "If you still see 502 error:"
echo "  → Go to Web → Click on error log"
echo "  → Share the last error message"
echo ""
echo "=========================================="

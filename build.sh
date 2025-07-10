#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files
python manage.py collectstatic --no-input

# 3. Apply database migrations
python manage.py migrate

# --- هذا هو السطر الجديد ---
# 4. Create a superuser if one doesn't exist
python manage.py create_superuser
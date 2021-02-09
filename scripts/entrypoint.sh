#!/bin/sh
set -e
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn -b 0.0.0.0:8000 -w 3 config.wsgi --reload --timeout 300 --keep-alive 50

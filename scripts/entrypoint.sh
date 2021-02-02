#!/bin/sh
set -e
# conda install -y -r /requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

gunicorn -b 0.0.0.0:8000 -w 5 config.wsgi --reload --timeout 300 --keep-alive 50
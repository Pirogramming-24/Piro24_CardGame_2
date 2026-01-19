#!/bin/sh
set -e

# 마이그레이션 및 기초 데이터 로드
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Starting Gunicorn Server..."
echo "Server is running now: http://localhost:8000"
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2
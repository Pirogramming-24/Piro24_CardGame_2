#!/bin/sh
set -e

# 마이그레이션 및 기초 데이터 로드
python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Starting Gunicorn Server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 2
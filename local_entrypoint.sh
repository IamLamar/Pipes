#!/bin/bash
set -e

echo "Waiting for PostgreSQL..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

echo "PostgreSQL started!"

# Выводим ключевые настройки Django перед миграциями
python manage.py shell -c "
from django.conf import settings
from django.apps import apps
from pprint import pprint

print('DJANGO_SETTINGS_MODULE =', settings.SETTINGS_MODULE)
print('PROD =', getattr(settings, 'PROD', None))
db = settings.DATABASES.get('default', {}).copy()
db.pop('PASSWORD', None)
print('DATABASE CONFIG (without password):')
pprint(db)
for app_label in ['apps.mainpage', 'apps.service_page', 'apps.products', 'apps.projects', 'apps.contacts', 'apps.company']:
    print(f'{app_label} installed =', apps.is_installed(app_label))
" || true

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Автоматическое создание суперпользователя
if [ -n "$SUPERUSER_USERNAME" ] && [ -n "$SUPERUSER_EMAIL" ] && [ -n "$SUPERUSER_PASSWORD" ]; then
  echo "Creating superuser..."
  python manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
username='$SUPERUSER_USERNAME'; \
email='$SUPERUSER_EMAIL'; \
password='$SUPERUSER_PASSWORD'; \
User.objects.filter(username=username).exists() or User.objects.create_superuser(username=username, email=email, password=password)"
fi

echo "Starting Django (Gunicorn)..."

gunicorn core.wsgi:application \
  --bind 0.0.0.0:8010 \
  --workers 3 \
  --timeout 120

release: python manage.py migrate
web: gunicorn config.wsgi:application
worker: celery worker --app=works_single_view.taskapp --loglevel=info

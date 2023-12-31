import os

from celery import Celery

# Configuração Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = Celery("api", broker="pyamqp://guest@rabbitmq/")

app.config_from_object("django.conf:settings")

app.autodiscover_tasks()

# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# create a Celery instance and configure it using the settings from Django
celery_app = Celery('myproject')

# Use a string here, as the configuration module is not yet configured
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

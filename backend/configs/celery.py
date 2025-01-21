import logging
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
logger = logging.getLogger('celery')

app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'handle_not_assigned_tasks': {
        'task': 'core.services.task_manager_service.assign_task_to_user',
        'schedule': crontab(minute="*/2")
    }
}

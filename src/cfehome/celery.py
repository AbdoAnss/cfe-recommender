import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')



app = Celery('cfehome')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run_subscription_avg_every_30': {
        'task': 'task_calculate_subscription_rating',
        'schedule': 60*30, # every 30 minutes
        'kwargs': {"all": True},
    }
}

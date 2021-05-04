'''
for running scheduled (periodic) tasks
'''

import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

# create a new instance of Celery
app = Celery("restaurant")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix. (to prevent overlap with other Django settings)
# add the Django settings module as a configuration source for Celery (can now configure Celery directly from the Django settings)
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load Celery tasks from all registered applications defined in settings.INSTALLED_APPS (following the tasks.py convention)
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
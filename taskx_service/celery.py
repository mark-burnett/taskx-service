from __future__ import absolute_import

from celery import Celery
from django.conf import settings


app = Celery(settings.TASKX_APP_NAME)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from __future__ import absolute_import

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings
import requests


LOG = get_task_logger(__name__)


app = Celery(settings.TASKX_APP_NAME)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app(bind=True, name='webhook')
def webhook(self, url, body_data):
    response = requests.patch(url, body_data,
                              headers={'Content-Type': 'application/json'})

    if int(response.status_code / 200) != 1:
        LOG.warn('Failed to deliver callback to %s', url)
        self.retry()

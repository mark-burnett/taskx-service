from . import settings
import importlib
import os


settings.BASE_DIR = os.path.dirname(importlib.import_module(
    settings.TASKX_APP_MODULE).__file__)


from . import celery


# flake8: noqa

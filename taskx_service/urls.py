from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles import views as static_views
import importlib

APP_URLS = importlib.import_module('%s.urls' % settings.TASKX_APP_MODULE)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^static/(?P<path>.*)$', static_views.serve),
] + APP_URLS.urlpatterns

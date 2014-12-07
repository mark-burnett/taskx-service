from django.conf import settings
from django.conf.urls import url, include
from rest_framework import routers
import importlib

views = importlib.import_module('%s.views' % settings.TASKX_APP_MODULE)

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]

"""sonar URL Configuration"""

from django.conf.urls import url, include
from .views import qa_metrics_home, qa_metrics_api

urlpatterns = [
    url(r'^$', qa_metrics_home, name='qa_metrics_home'),
    url(r'^(?P<project_id>[0-9]+)/(?P<start_date>[0-9 + : T -]+)/(?P<end_date>[0-9 + : T -]+)/$', qa_metrics_api, name='qa_metrics_api'),
]

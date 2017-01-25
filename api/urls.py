"""sonar URL Configuration"""

from django.conf.urls import url, include
from .views import chart

urlpatterns = [
    url(r'^(?P<component_id>[0-9]+)/(?P<start_date>[0-9 + : T -]+)/(?P<end_date>[0-9 + : T -]+)/$', chart, name='home'),
]

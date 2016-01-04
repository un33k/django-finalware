from django.conf.urls import url
from django.conf.urls import patterns

from . import views


urlpatterns = [
    url(
        r'^make_request/$',
        views.request_processor,
        name='make_request'
    ),
]

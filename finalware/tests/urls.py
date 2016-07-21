from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^make_request/$',
        views.request_processor,
        name='make_request'
    ),
]

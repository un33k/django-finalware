from django.conf.urls import patterns

from . import views


urlpatterns = patterns('',
    (r'^make_request/$', views.request_processor),
)

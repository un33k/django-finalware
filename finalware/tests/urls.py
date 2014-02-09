from django.contrib import admin
from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^admin', include(admin.site.urls)),
)

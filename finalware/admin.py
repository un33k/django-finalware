from django.contrib import admin
from django.contrib.sites.models import Site



class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'name',)
    search_fields = ('domain', 'name', 'id',)
    ordering = ('id', 'domain')

try:
    admin.site.unregister(Site)
except:
    pass
admin.site.register(Site, SiteAdmin)

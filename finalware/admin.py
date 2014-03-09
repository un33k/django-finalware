from django.contrib import admin
from django.contrib.sites.models import Site

from . import defaults


# Adding the Site models to the admin page
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'name',)
    search_fields = ('domain', 'name', 'id',)
    ordering = ('id', 'domain')

try:
    admin.site.unregister(Site)
except admin.sites.NotRegistered:
    pass
admin.site.register(Site, SiteAdmin)


# Adding the Session models to the admin page
if defaults.SITE_ENABLE_SESSION_IN_ADMIN:
    import pprint
    from django.contrib.sessions.models import Session

    class SessionAdmin(admin.ModelAdmin):

        def _session_data(self, obj):
            return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
        _session_data.allow_tags = True
        list_display = ['session_key', '_session_data', 'expire_date']
        readonly_fields = ['_session_data']
        exclude = ['session_data']
        date_hierarchy = 'expire_date'

    try:
        admin.site.unregister(Session)
    except admin.sites.NotRegistered:
        pass

    admin.site.register(Session, SessionAdmin)

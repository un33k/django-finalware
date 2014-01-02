from django.conf import settings
from django.contrib.sites.models import Site
from django import template

from . import defaults



# Setup the available sites for this project
def load_site_objects():
    """
    Load the available Sites for this project.
    `SITE_ID` in the settings file will decide the `current` site object.
    """
    site_info = getattr(defaults, 'SITE_OBJECTS_INFO_DICT')
    if site_info:
        for pk in sorted(site_info.iterkeys()):
            site, created = Site.objects.get_or_create(pk=pk)
            if site:
                site.name = site_info[pk]['name']
                site.domain = site_info[pk]['domain']
                site.save()

def load_template_tags():
    """
    Loads template tags found in SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST on startup
    """
    for t in defaults.SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST:
        template.add_to_builtins(t)

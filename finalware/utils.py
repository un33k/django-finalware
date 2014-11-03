import logging
from django.conf import settings
from django.apps import apps
from django.contrib.sites.models import Site
from django.template.base import add_to_builtins

from . import defaults as defs

log = logging.getLogger(__name__)


# Setup the available sites for this project
def load_site_objects(verbosity):
    """
    Load the available Sites for this project.
    `SITE_ID` in the settings file will decide the `current` site object.
    """
    if not apps.is_installed('django.contrib.sites'):
        return
    site_info = getattr(defs, 'SITE_OBJECTS_INFO_DICT')
    if site_info:
        for pk in sorted(site_info.keys()):
            site, created = Site.objects.get_or_create(pk=pk)
            if site:
                site.name = site_info[pk]['name']
                site.domain = site_info[pk]['domain']
                site.save()
                if verbosity >= 2:
                    if created:
                        print('Creating {} Site'.format(site.domain))
                    else:
                        print('Updated {} Site'.format(site.domain))


def load_template_tags():
    """
    Loads template tags found in SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST on startup
    """
    for t in defs.SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST:
        add_to_builtins(t)


def create_superuser(verbosity):
    """
    Create or update a superuser.
    """
    user_id = getattr(defs, 'SITE_SUPERUSER_ID')
    username = getattr(defs, 'SITE_SUPERUSER_USERNAME')
    email = getattr(defs, 'SITE_SUPERUSER_EMAIL')
    password = getattr(defs, 'SITE_SUPERUSER_PASSWORD')
    if user_id and username and email and password:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user, created = User.objects.get_or_create(pk=user_id)
        if user:
            if hasattr(user, 'username'):
                user.username = username
            if hasattr(user, 'email'):
                user.email = email
            user.set_password(password)
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
            user.save()
            log.info('Superuser created or updated')
            if verbosity >= 2:
                if created:
                    print('Creating superuser')
                else:
                    print('Updated superuser')

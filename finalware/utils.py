import logging
from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext as _

from . import defaults

log = logging.getLogger(__name__)


# Setup the available sites for this project
def load_site_objects():
    """
    Load the available Sites for this project.
    `SITE_ID` in the settings file will decide the `current` site object.
    """
    site_info = getattr(defaults, 'SITE_OBJECTS_INFO_DICT')
    if site_info:
        for pk in sorted(site_info.keys()):
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


def create_superuser():
    """
    Create or update a superuser.
    """
    user_id = getattr(settings, 'SITE_SUPERUSER_ID', '')
    username = getattr(settings, 'SITE_SUPERUSER_USERNAME', '')
    email = getattr(settings, 'SITE_SUPERUSER_EMAIL', '')
    password = getattr(settings, 'SITE_SUPERUSER_PASSWORD', '')
    if user_id and username and email and password:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user, created = User.objects.get_or_create(pk=user_id)
        if user:
            user.set_password(password)
            setattr(user, user.USERNAME_FIELD, username)
            if hasattr(user, 'email'):
                user.email = email
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
            user.save()
            log.info(_('Superuser created/updated'))


def is_last_installed_app(app_config):
    """
    Returns True if this app is the last installed application
    Returns False if this app is not installed or not the last application
    """
    if app_config.label == settings.INSTALLED_APPS[-1].split('.')[-1]:
        return True
    return False

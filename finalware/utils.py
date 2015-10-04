import logging
from django.conf import settings
from django.apps import apps
from django.contrib.sites.models import Site

from . import defaults as defs

log = logging.getLogger(__name__)


def load_template_tags():
    """
    Loads template tags found in SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST on startup
    """
    try:
        from django.template.base import add_to_builtins
        for t in defs.SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST:
            add_to_builtins(t)
        log.info('Loaded default template tags')
    except ImportError:
        log.info('Use builtins option of the TEMPLATES list in your settings.')


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


def create_superuser(verbosity):
    """
    Create or update a superuser.
    """
    username = getattr(defs, 'SITE_SUPERUSER_USERNAME')
    email = getattr(defs, 'SITE_SUPERUSER_EMAIL')
    password = getattr(defs, 'SITE_SUPERUSER_PASSWORD')
    if not password:
        print('Skipped superuser create/update. No password supplied.')
        return

    from django.contrib.auth import get_user_model
    User = get_user_model()
    if User.USERNAME_FIELD == 'email' and email:
        user, created = User.objects.get_or_create(email=email)
    elif User.USERNAME_FIELD == 'username' and username:
        user, created = User.objects.get_or_create(username=username)
    else:
        print('Skipped superuser create/update. No username or email supplied.')
        return

    if not created and not user.is_superuser:
        print('Unable to promote normal user to superuser. Use createsuperuser command.')
        return

    if email and hasattr(user, 'email'):
        user.email = email
    if username and hasattr(user, 'username'):
        user.username = username
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

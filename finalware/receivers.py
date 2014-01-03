import logging

from django.conf import settings
from django.db.models import signals

from .utils import load_site_objects
from .utils import load_template_tags
from .utils import create_superuser

log = logging.getLogger("{}.{}".format('__module__', '__name__'))


def disable_superuser_request():
    """
    Disable syncdb prompting for superuser creation.
    """
    from django.contrib.auth import models as auth_model
    from django.contrib.auth.management import create_superuser as django_create_superuser
    signals.post_syncdb.disconnect(
        django_create_superuser,
        sender=auth_model,
        dispatch_uid = "django.contrib.auth.management.create_superuser"
    )

def finalize(sender, **kwargs):
    """
    After syncdb/migrate, make final adjustments in order to prepare
    and secure the site. At the end of the function, the site is up and
    ready to accept requests.
    """
    # only trigger if we have installed the last app
    if kwargs['app'].__name__ == '{}.models'.format(settings.INSTALLED_APPS[-1]):

        # setup sites
        load_site_objects()

        # load commonly used template tags, once upon start
        load_template_tags()

        # do other site-wide related stuff here

        # the last thing is to create or update a superuser
        create_superuser()

# Disconnect superuser creation
if getattr(settings, 'SITE_SUPERUSER_ID', False):
    disable_superuser_request()

# Latch to post syncdb signal
signals.post_syncdb.connect(finalize)

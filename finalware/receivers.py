import logging

from django.conf import settings
from django.db.models import signals
from django.apps import apps

from .utils import load_site_objects
from .utils import load_template_tags
from .utils import create_superuser
from .utils import is_last_installed_app


log = logging.getLogger(__name__)


def disable_create_superuser_request(sender, **kwargs):
    """
    Disable migrate prompting for superuser creation.
    """
    if is_last_installed_app(kwargs['app_config']):
        from django.contrib.auth.management import create_superuser as django_create_superuser
        signals.post_migrate.disconnect(
            django_create_superuser,
            sender=apps.get_app_config('auth'),
            dispatch_uid="django.contrib.auth.management.create_superuser"
        )

signals.pre_migrate.connect(disable_create_superuser_request)


def finalize(sender, **kwargs):
    """
    After migrate, make final adjustments in order to prepare
    and secure the site. At the end of the function, the site is up and
    ready to accept requests.
    """
    if is_last_installed_app(kwargs['app_config']):
        # setup sites
        load_site_objects()

        # load commonly used template tags, once upon start
        load_template_tags()

        # the last thing is to create or update a superuser
        if getattr(settings, 'SITE_SUPERUSER_ID', False):
            create_superuser()

# Latch to post migrate signal
signals.post_migrate.connect(finalize)

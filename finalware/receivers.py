import logging

from django.conf import settings
from django.db.models import signals
from django.apps import apps
from django.db import DEFAULT_DB_ALIAS

from .utils import load_site_objects
from .utils import create_superuser

from . import defaults as defs

log = logging.getLogger(__name__)


def pre_migrate_receiver(app_config, verbosity=2, interactive=False, using=DEFAULT_DB_ALIAS, **kwargs):
    """
    Disable the superuser creation prompt.
    """
    from django.contrib.auth import management
    if hasattr(management, 'create_superuser'):
        signals.post_migrate.disconnect(
            management.create_superuser,
            sender=apps.get_app_config('auth'),
            dispatch_uid="django.contrib.auth.management.create_superuser"
        )
        if verbosity >= 2:
            print("Disabling create_superuser prompt")


def post_migrate_receiver(app_config, verbosity=2, interactive=False, using=DEFAULT_DB_ALIAS, **kwargs):
    """
    Finalize the website loading.
    """
    load_site_objects(verbosity)
    create_superuser(verbosity)

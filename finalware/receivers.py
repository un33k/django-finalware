import logging

from django.conf import settings
from django.db.models import signals
from django.apps import apps

from .utils import load_site_objects
from .utils import load_template_tags
from .utils import create_superuser


log = logging.getLogger(__name__)

__all__ = ['pre_migrate_receiver', 'post_migrate_receiver', ]


class PreMigrateReceiver(object):
    """
    Disable the superuser creation prompt.
    """
    def __init__(self):
        self.call_counter = 0

    def __call__(self, signal, sender, **kwargs):
        self.call_counter += 1
        if self.call_counter == 1:
            from django.contrib.auth import management
            signals.post_migrate.disconnect(
                management.create_superuser,
                sender=apps.get_app_config('auth'),
                dispatch_uid="django.contrib.auth.management.create_superuser"
            )

pre_migrate_receiver = PreMigrateReceiver()


class PostMigrateReceiver(object):
    """
    Finalize the website loading.
    """
    def __init__(self):
        self.call_counter = 0

    def __call__(self, signal, sender, **kwargs):
            self.call_counter += 1
            if self.call_counter == 1:
                load_site_objects()
                load_template_tags()
                if getattr(settings, 'SITE_SUPERUSER_ID', False):
                    create_superuser()

post_migrate_receiver = PostMigrateReceiver()

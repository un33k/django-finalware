from django.db.models import signals
from django.apps import apps
from django.apps import AppConfig as DjangoAppConfig

from . import receivers


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the finalware app
    """
    label = name = 'finalware'
    verbose_name = 'finalware, a bootstrap app'

    def ready(self):
        """
        App is imported and ready, so bootstrap it.
        """
        signals.pre_migrate.connect(receivers.pre_migrate_receiver,
            sender=apps.get_app_config('auth'))

        signals.post_migrate.connect(receivers.post_migrate_receiver,
            sender=apps.get_app_config(self.name))

from django.db.models import signals
from django.apps import apps
from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the finalware app
    """
    name = 'finalware'
    verbose_name = 'Finalware App'

    def ready(self):
        """
        App is imported and ready, so bootstrap it.
        """
        from . import receivers as rcvs

        signals.pre_migrate.connect(rcvs.pre_migrate_receiver,
            sender=apps.get_app_config('auth'))

        signals.post_migrate.connect(rcvs.post_migrate_receiver,
            sender=apps.get_app_config(self.name))

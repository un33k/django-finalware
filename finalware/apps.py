from django.db.models import signals
from django.apps import apps
from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import ugettext_lazy as _

from . import receivers


class AppConfig(DjangoAppConfig):
    """
    Configuration entry point for the finalware app
    """
    label = name = 'finalware'
    verbose_name = _("finalware, a bootstrap app")

    def ready(self):
        """
        App is ready.
        """
        signals.pre_migrate.connect(receivers.pre_migrate_receiver,
            sender=apps.get_app_config('auth'))

        signals.post_migrate.connect(receivers.post_migrate_receiver,
            sender=self)

        receivers.load_template_tags()

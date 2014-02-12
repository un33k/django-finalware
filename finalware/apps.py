from django.db.models import signals
from django.apps import apps, AppConfig
from django.utils.translation import ugettext_lazy as _

from . import receivers


class FinalwareConfig(AppConfig):
    """
    Configuration entry point for the finalware app
    """
    name = 'finalware'
    verbose_name = _("finalware, a bootstrap app")

    def ready(self):
        signals.pre_migrate.connect(receivers.pre_migrate_receiver,
            sender=apps.get_app_config('auth'))
        signals.post_migrate.connect(receivers.post_migrate_receiver,
            sender=self)

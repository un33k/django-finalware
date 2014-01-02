from django.db.models import signals

from .utils import finalize_site



# Latch to post syncdb signal
signals.post_syncdb.connect(finalize_site)

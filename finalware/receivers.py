from django.db.models import signals

from .utils import finalize



# Latch to post syncdb signal
signals.post_syncdb.connect(finalize)

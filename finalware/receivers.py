from django.conf import settings
from django.db.models import signals

from .utils import load_site_objects
from .utils import load_template_tags


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

# Latch to post syncdb signal
signals.post_syncdb.connect(finalize)

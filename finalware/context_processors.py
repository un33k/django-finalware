from django.contrib.sites.models import Site

from . import defaults


# Current Site Object (site: name, site: domain)
SITE_OBJECT_CURRENT = Site.objects.get_current()


def contextify(request):
    """
    Injects some optional data into the context.
    """
    ctx = {
        'SITE_ORGANIZATION': defaults.SITE_ORGANIZATION,
        'SITE_NAME': defaults.SITE_NAME,
        'SITE_DOMAIN': defaults.SITE_DOMAIN,
        'SITE_PROTOCOL': defaults.SITE_PROTOCOL or request.is_secure() and 'https' or 'http',
        'SITE_TITLE': defaults.SITE_TITLE,
        'SITE_KEYWORDS': defaults.SITE_KEYWORDS,
        'SITE_DESCRIPTION': defaults.SITE_DESCRIPTION,
        'SITE_CDN_STATIC_URL': defaults.SITE_CDN_STATIC_URL,
        'SITE_CDN_MEDIA_URL': defaults.SITE_CDN_MEDIA_URL,
        'SITE_GOOGLE_ANALYTICS': defaults.SITE_GOOGLE_ANALYTICS,
        'SITE_OBJECT_CURRENT': SITE_OBJECT_CURRENT,
    }

    ctx.update(defaults.SITE_EXTRA_CONTEXT_DICT)

    return ctx

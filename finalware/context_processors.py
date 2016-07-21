from django.contrib.sites.models import Site

from . import defaults


# Current Site Object (site: name, site: domain)
SITE_OBJECT_CURRENT = Site.objects.get_current()


def contextify(request):
    """
    Injects some optional data into the context.
    """
    ctx = {}
    if defaults.SITE_ORGANIZATION:
        ctx['SITE_ORGANIZATION'] = defaults.SITE_ORGANIZATION
    if defaults.SITE_NAME:
        ctx['SITE_NAME'] = defaults.SITE_NAME
    if defaults.SITE_DOMAIN:
        ctx['SITE_DOMAIN'] = defaults.SITE_DOMAIN
    if defaults.SITE_PROTOCOL:
        ctx['SITE_PROTOCOL'] = defaults.SITE_PROTOCOL or request.is_secure() and 'https' or 'http'
    if defaults.SITE_TITLE:
        ctx['SITE_TITLE'] = defaults.SITE_TITLE
    if defaults.SITE_KEYWORDS:
        ctx['SITE_KEYWORDS'] = defaults.SITE_KEYWORDS
    if defaults.SITE_DESCRIPTION:
        ctx['SITE_DESCRIPTION'] = defaults.SITE_DESCRIPTION
    if defaults.SITE_CDN_STATIC_URL:
        ctx['SITE_CDN_STATIC_URL'] = defaults.SITE_CDN_STATIC_URL
    if defaults.SITE_CDN_MEDIA_URL:
        ctx['SITE_CDN_MEDIA_URL'] = defaults.SITE_CDN_MEDIA_URL
    if defaults.SITE_GOOGLE_ANALYTICS:
        ctx['SITE_GOOGLE_ANALYTICS'] = defaults.SITE_GOOGLE_ANALYTICS
    if SITE_OBJECT_CURRENT:
        ctx['SITE_OBJECT_CURRENT'] = SITE_OBJECT_CURRENT

    ctx.update(defaults.SITE_EXTRA_CONTEXT_DICT)

    return ctx

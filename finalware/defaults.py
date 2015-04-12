from django.conf import settings

# Super user account info
SITE_SUPERUSER_USERNAME = getattr(settings, 'SITE_SUPERUSER_USERNAME', None)
SITE_SUPERUSER_EMAIL = getattr(settings, 'SITE_SUPERUSER_EMAIL', None)
SITE_SUPERUSER_PASSWORD = getattr(settings, 'SITE_SUPERUSER_PASSWORD', None)

# ID of the current site object
SITE_ID = getattr(settings, 'SITE_ID', None)

# Automatically create the site objects for this website
SITE_OBJECTS_INFO_DICT = getattr(settings, 'SITE_OBJECTS_INFO_DICT', None)

# Site's CDN Static URL (e.g. Amazon S3 bucket configured for downloading)
SITE_CDN_STATIC_URL = getattr(settings, 'SITE_CDN_STATIC_URL', '')

# Site's CDN Media URL (e.g. Amazon S3 bucket configured for streaming)
SITE_CDN_MEDIA_URL = getattr(settings, 'SITE_CDN_MEDIA_URL', '')

# Site's CDN Upload URL (e.g. Amazon S3 bucket configured for uploads)
SITE_CDN_UPLOAD_URL = getattr(settings, 'SITE_CDN_UPLOAD_URL', '')

# Site Specific Info
SITE_ORGANIZATION = getattr(settings, 'SITE_ORGANIZATION', 'Example Org')
SITE_NAME = getattr(settings, 'SITE_PROJ_NAME', 'Example Site')
SITE_DOMAIN = getattr(settings, 'SITE_DOMAIN_NAME', 'example.com')
SITE_PROTOCOL = getattr(settings, 'SITE_PROTOCOL', None)
SITE_TITLE = getattr(settings, 'SITE_TITLE', SITE_DOMAIN.upper())
SITE_KEYWORDS = getattr(settings, 'SITE_KEYWORDS', 'Example Org Related Keywords')
SITE_DESCRIPTION = getattr(settings, 'SITE_DESCRIPTION', 'Example Org is a Django-Powered Site.')

# Google Analytics for this site
SITE_GOOGLE_ANALYTICS = getattr(settings, 'SITE_GOOGLE_ANALYTICS', '')

# Auto-load template tags in this list
SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST = getattr(settings, 'SITE_TEMPLATE_TAGS_AUTO_LOAD_LIST', {})

# To see session objects in admin
SITE_ENABLE_SESSION_IN_ADMIN = getattr(settings, 'SITE_ENABLE_SESSION_IN_ADMIN', False)

# Extra context
SITE_EXTRA_CONTEXT_DICT = getattr(settings, 'SITE_EXTRA_CONTEXT_DICT', {})

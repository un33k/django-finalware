Django Finalware
====================

**A utility application that finalizes the bootstrapping of a Django-powered site**

[![build-status-image-fury]][fury]
[![build-status-image-pypi]][pypi]


Overview
====================

This utility application automatically setup the `Site` objects and injects any site related
data into the response context. It also auto loads the most used template tags upfront.

How to install
====================

    1. easy_install django-finalware
    2. pip install django-finalware
    3. git clone http://github.com/un33k/django-finalware
        a. cd django-finalware
        b. run python setup.py
    4. wget https://github.com/un33k/django-finalware/zipball/master
        a. unzip the downloaded file
        b. cd into django-finalware-* directory
        c. run python setup.py


How to use
====================

   # Add `finalware` to the very end of your INSTALLED_APPS
   ```python
    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.humanize',
        'django.contrib.admin',


        # last application to finalize things
        'finalware',
    ]
   ```

   # Add `finalware` to the very end of your TEMPLATE_CONTEXT_PROCESSORS
   ```python
    TEMPLATE_CONTEXT_PROCESSORS = [
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.request',

        'finalware.context_processors.contextify',
    ]
   ```

   # Setup your SITE_OBJECTS_INFO_DICT
   ```python
    SITE_OBJECTS_INFO_DICT = {
        '1': {
            'name': 'production',
            'domain': 'example.com',
        },
        '2':{
            'name': 'integration',
            'domain': 'example.org'
        },
        '3':{
            'name': 'development',
            'domain': '192.168.1.20:8080'
        },
    }
    SITE_ID = 1
   ```


Advanced users:
====================

   # To automatically load the common template tags, add the following to your settings file
   ```python
    AUTO_LOAD_TEMPLATE_TAGS_LIST = [
        # django specific tags
        'django.templatetags.cache',
        'django.templatetags.future',
        'django.templatetags.i18n',
        'django.templatetags.l10n',
        'django.templatetags.static',
        'django.contrib.humanize.templatetags.humanize',

        # 3rd party tags
    ]

   ```

   # If any of the following is set in your settings file, they automatically get inject into the context
   ```python
    # Site's CDN Static URL (e.g. Amazon S3 bucket configured for downloading)
    SITE_CDN_STATIC_URL = ''

    # Site's CDN Media URL (e.g. Amazon S3 bucket configured for streaming)
    SITE_CDN_MEDIA_URL = ''

    # Site's CDN Upload URL (e.g. Amazon S3 bucket configured for uploads)
    SITE_CDN_UPLOAD_URL = ''

    # Site Specific Info
    SITE_ORGANIZATION = ''
    SITE_NAME = ''
    SITE_DOMAIN = ''
    SITE_PROTOCOL = ''
    SITE_TITLE = ''
    SITE_KEYWORDS = ''
    SITE_DESCRIPTION = ''
    SITE_GOOGLE_ANALYTICS = ''
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under ([BSD](LICENSE.md)).


[build-status-image-travis]: https://secure.travis-ci.org/un33k/django-finalware.png?branch=master
[travis]: http://travis-ci.org/tomchristie/django-finalware?branch=master

[build-status-image-fury]: https://badge.fury.io/py/django-finalware.png
[fury]: http://badge.fury.io/py/django-finalware

[build-status-image-pypi]: https://pypip.in/d/django-finalware/badge.png
[pypi]: https://crate.io/packages/django-finalware?version=latest


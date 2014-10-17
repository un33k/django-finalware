Django Finalware
====================

**A utility application that automates the bootstrapping of a Django-powered site**

[![build-status-image-travis]][travis]
[![build-status-image-fury]][fury]
[![build-status-image-pypi]][pypi]


Overview
====================

This utility application can automatically:

  1. Setup the `Site` objects for (development, integration & production)
  2. Inject common site related data into the response `context`
  3. Load the most-used `template tags` on startup
  4. Create and/or update a `superuser` account

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

Compatibility
====================
    1. Please use version 0.0.2 for Django<=1.6.x
    2. Otherwise refer to the ([build matrix](.travis.yml)).

How to use
====================

   ```python

    # Add `finalware` to the very end of your INSTALLED_APPS

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

   ```python

    # Add `finalware.context_processors.contextify` to your TEMPLATE_CONTEXT_PROCESSORS

    TEMPLATE_CONTEXT_PROCESSORS = [
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.request',

        'finalware.context_processors.contextify',
    ]

   ```

   ```python

    # Add `SITE_OBJECTS_INFO_DICT` to your settings file. For example:

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

   ```python

    # To create/update a superuser account automatically, add the following to your settings file.
    # This will disable the `superuser` creation option of syncdb.

    # This field is the superuser object ID. Pick something other than `1` for security reason.
    SITE_SUPERUSER_ID = ''

    # This field is stored in `User.USERNAME_FIELD`. This is usually a `username` or  an `email`.
    SITE_SUPERUSER_USERNAME = ''

    # This field is stored in the `email` field, provided, that `User.USERNAME_FIELD` is not an `email`.
    # If `User.USERNAME_FIELD` is already an email address, set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
    SITE_SUPERUSER_EMAIL = ''

    # A hashed version of `SITE_SUPERUSER_PASSWORD` will be store in superuser's `password` field.
    SITE_SUPERUSER_PASSWORD = ''

   ```

   ```python

    # To automatically load the most-used template tags, add them to `AUTO_LOAD_TEMPLATE_TAGS_LIST` in your settings.

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

   ```python

    # To automatically add any of the following to your response context, set them in your settings file.

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

   ```python

   # To add any extra data to your response context, set SITE_EXTRA_CONTEXT_DICT in your settings file.

   SITE_EXTRA_CONTEXT_DICT = {
       "key_1": "value_1",
       "key_2": "value_2",
       "key_3": "value_3",
       # ...
   }
   ```

Running the tests
====================

To run the unit test:

    python manage.py test


License
====================

Released under a ([BSD](LICENSE.md)) license.


[build-status-image-travis]: https://secure.travis-ci.org/un33k/django-finalware.png?branch=master
[travis]: http://travis-ci.org/un33k/django-finalware?branch=master

[build-status-image-fury]: https://badge.fury.io/py/django-finalware.png
[fury]: http://badge.fury.io/py/django-finalware

[build-status-image-pypi]: https://pypip.in/d/django-finalware/badge.png
[pypi]: https://crate.io/packages/django-finalware?version=latest

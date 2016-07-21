## 0.1.4

Enhancements:

  - Remove Template Tag loading option as you can set that in settings.py now
  - Drop support for python 3.3
  - Update supported Django to 1.9.8 and 1.8.14

## 0.1.4

Bugfix:

  - Change SITE_DOMAIN_NAME to SITE_DOMAIN (second attempt)

## 0.1.3

Enhancements:

  - Change SITE_DOMAIN_NAME to SITE_DOMAIN
  - Prepare for Django 1.10

## 0.1.2

Enhancements:

  - Make app registry load modules on ready() in preparation for Django 1.9

## 0.1.1

Enhancements:

  - Make template tags loading optional in preparation for Django 1.9

## 0.1.0

Enhancements:

  - Add 1.8 and drop <=1.6.x
  - Beta version
  - Dropped SITE_SUPERUSER_ID as django 1.8 allows for UUID as primary key

## 0.0.8

Enhancements:

  - Better handle multiple post-migrate signals.

## 0.0.7

Enhancements:

  - Travis configuration rework.
  - Dropped compatibility table from readme.

## 0.0.6

Features:

  - Added support for pyp3

## 0.0.6

Features:

  - Added support for 3.4 and pypy

## 0.0.5

Features:

  - Added the ability to inject extra data into response context via settings.SITE_EXTRA_CONTEXT_DICT

Bug fix:

  - Loading template tags is moved to the ready() function

## 0.0.4

Bug fix:

  - Fix unit tests
  - Test for pre and post migration signals

## 0.0.3

Features:

  - Django 1.7 support (backward incompatible)
    - Note: Use version (0.0.2) for Django <= 1.6.x

## 0.0.2

Features:

  - Python 3.x support

## 0.0.1

Features:

  - Initial Release

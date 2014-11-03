## 0.0.8

Enhancements:

  - Better handle multiple post-migrate signals.

## 0.0.7

Enhancements:

  - Travis configuration rework.
  - Dropped compatibility table from readme.

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

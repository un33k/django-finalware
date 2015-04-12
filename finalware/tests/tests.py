from django.test import TestCase
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model


from finalware import defaults
from finalware.utils import load_site_objects
from finalware.utils import create_superuser
from finalware.receivers import pre_migrate_receiver
from finalware.receivers import post_migrate_receiver

User = get_user_model()


class SiteTestCase(TestCase):
    """
    Site objects are created
    """

    def setUp(self):
        self.resp = self.client.get('/make_request/')
        self.assertEqual(self.resp.status_code, 200)

    def test_default_site_object(self):
        sites = Site.objects.count()
        self.assertEqual(sites, 3)

    def test_current_site_object(self):
        curr = Site.objects.get_current()
        self.assertEqual(curr.id, defaults.SITE_ID)

    def test_total_site_objects(self):
        load_site_objects(verbosity=1)
        sites = Site.objects.count()
        self.assertEqual(sites, len(defaults.SITE_OBJECTS_INFO_DICT))


class ContextTestCase(TestCase):
    """
    Context is filled in
    """
    def setUp(self):
        self.resp = self.client.get('/make_request/')
        self.assertEqual(self.resp.status_code, 200)

    def test_context_site(self):
        curr_site = Site.objects.get_current()
        self.assertEqual(self.resp.context['SITE_OBJECT_CURRENT'], curr_site)

    def test_context_protocol(self):
        self.assertEqual(self.resp.context['SITE_PROTOCOL'], 'http')

    def test_context_organization(self):
        self.assertEqual(self.resp.context['SITE_ORGANIZATION'], defaults.SITE_ORGANIZATION)

    def test_context_name(self):
        self.assertEqual(self.resp.context['SITE_NAME'], defaults.SITE_NAME)

    def test_context_domain(self):
        self.assertEqual(self.resp.context['SITE_DOMAIN'], defaults.SITE_DOMAIN)

    def test_context_title(self):
        self.assertEqual(self.resp.context['SITE_TITLE'], defaults.SITE_TITLE)

    def test_context_description(self):
        self.assertEqual(self.resp.context['SITE_DESCRIPTION'], defaults.SITE_DESCRIPTION)


class ExtraContextTestCase(TestCase):
    """
    Extra Context is filled in
    """
    def setUp(self):
        self.resp = self.client.get('/make_request/')
        self.assertEqual(self.resp.status_code, 200)

    def test_context_site(self):
        curr_site = Site.objects.get_current()
        self.assertEqual(self.resp.context['SITE_OBJECT_CURRENT'], curr_site)

    def test_context_valid_key_1(self):
        self.assertEqual(self.resp.context['key_1'], 'value_1')

    def test_context_valid_key_2(self):
        self.assertEqual(self.resp.context['key_2'], 'value_2')

    def test_context_valid_key_3(self):
        self.assertEqual(self.resp.context['key_3'], 'value_3')

    def test_context_invalid_key_4(self):
        self.assertEqual('key_4' in self.resp.context, False)


class SuperuserTestCase(TestCase):
    """
    Site objects are created
    """
    def setUp(self):
        create_superuser(verbosity=1)
        self.user = User.objects.get(email=settings.SITE_SUPERUSER_EMAIL)

    def test_one_user(self):
        users = User.objects.count()
        self.assertEqual(users, 1)

    def test_superuser_username(self):
        username_field = self.user.USERNAME_FIELD
        if hasattr(self.user, username_field):
            self.assertEqual(getattr(self.user, username_field), settings.SITE_SUPERUSER_USERNAME)

    def test_superuser_email(self):
        if hasattr(self.user, 'email'):
            self.assertEqual(self.user.email, settings.SITE_SUPERUSER_EMAIL)

    def test_superuser_password(self):
        self.assertEqual(self.user.check_password(settings.SITE_SUPERUSER_PASSWORD), True)

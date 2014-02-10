from django.test import TestCase
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.test.utils import setup_test_environment


from finalware import defaults


class SiteTestCase(TestCase):
    """
    Site objects are created
    """

    def setUp(self):
        setup_test_environment()
        self.resp = self.client.get('/make_request/')
        self.assertEqual(self.resp.status_code, 200)

    def test_current_site_object(self):
        curr = Site.objects.get_current()
        self.assertEquals(curr.id, defaults.SITE_ID)

    def test_total_site_objects(self):
        sites = Site.objects.count()
        self.assertEquals(sites, len(defaults.SITE_OBJECTS_INFO_DICT))


class ContextTestCase(TestCase):
    """
    Context is filled in
    """
    def setUp(self):
        setup_test_environment()
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


class SuperuserTestCase(TestCase):
    """
    Site objects are created
    """
    def setUp(self):
        setup_test_environment()
        User = get_user_model()
        self.user = User.objects.get(pk=settings.SITE_SUPERUSER_ID)

    def test_superuser_username(self):
        username_field = self.user.USERNAME_FIELD
        if hasattr(self.user, username_field):
            self.assertEquals(getattr(self.user, username_field), settings.SITE_SUPERUSER_USERNAME)

    def test_superuser_email(self):
        if hasattr(self.user, 'email'):
            self.assertEquals(self.user.email, settings.SITE_SUPERUSER_EMAIL)

    def test_superuser_password(self):
        self.assertEquals(self.user.check_password(settings.SITE_SUPERUSER_PASSWORD), True)

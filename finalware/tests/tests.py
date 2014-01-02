from django.test import TestCase
from django.contrib.sites.models import Site

from finalware import defaults

class SiteObjectTestCase(TestCase):
    """
    Site objects are created
    """
    def setUp(self):
        pass

    def test_current_site_object(self):
        curr = Site.objects.get_current()
        self.assertEquals(curr.id, defaults.SITE_ID)

    def test_total_site_objects(self):
        sites = Site.objects.count()
        self.assertEquals(sites, len(defaults.SITE_OBJECTS_INFO_DICT))


class SiteUpTestCase(TestCase):
    """
    Django is up and running
    """
    def setUp(self):
        self.resp = self.client.get('/admin')

    def test_admin_page(self):
        self.assertEqual(self.resp.status_code, 200)


class ContextTestCase(TestCase):
    """
    Context is filled in
    """
    def setUp(self):
        self.resp = self.client.get('/admin')

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

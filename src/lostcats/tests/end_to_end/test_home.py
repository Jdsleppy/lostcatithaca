from django import test

from django.urls import reverse


class TestHome(test.TestCase):
    def setUp(self):
        self.url = reverse("home")

    def test_fetch(self):
        """The homepage should be rendered with 200 OK."""
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lostcats/home.html")

    def test_fetch_debug_no_analytics(self):
        """Do not render the analytics tag in dev."""
        with self.settings(DEBUG=True):
            resp = self.client.get(self.url)
            self.assertNotContains(resp, "data-goatcounter")

        with self.settings(DEBUG=False):
            resp = self.client.get(self.url)
            self.assertContains(resp, "data-goatcounter")

    def test_page_title_default(self):
        """When the page title is not overridden,
        it should default to LostCat Ithaca.
        """
        resp = self.client.get(self.url)

        self.assertContains(resp, "<title>LostCat Ithaca</title>", count=1)

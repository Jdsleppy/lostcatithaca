from django import test

from django.urls import reverse


class TestCatLocate(test.TestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("cat-locate")

    def test_fetch(self):
        """The page should be rendered with 200 OK."""
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lostcats/cat_locate.html")

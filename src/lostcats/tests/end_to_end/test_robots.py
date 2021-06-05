from django import test

from django.urls import reverse


class TestRobots(test.TestCase):
    def setUp(self):
        self.url = reverse("robots")

    def test_fetch(self):
        """A robots.txt allowing all crawlers should be rendered."""
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lostcats/robots.txt")
        self.assertContains(resp, "User-agent: *\nAllow: /")

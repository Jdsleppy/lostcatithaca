from django.urls import reverse

from lostcats.tests.utils import TemporaryMediaTestCase
from lostcats.tests.factories import LostCatFactory
from lostcats.serializers import cat_serializer


class TestCatDetail(TemporaryMediaTestCase):
    def setUp(self):
        super().setUp()
        self.cat = LostCatFactory()
        self.url = reverse(
            "cat-detail", kwargs=dict(pk=self.cat.pk, slug=self.cat.slug)
        )

    def test_fetch_not_found(self):
        """Fetching a nonexistent cat should 404."""
        resp = self.client.get(
            reverse("cat-detail", kwargs=dict(pk=12345, slug="the-wrong-slug"))
        )

        self.assertTemplateNotUsed(resp, "lostcats/cat_detail.html")
        self.assertEqual(resp.status_code, 404)

    def test_fetch(self):
        """Fetching a cat should render the cat detail template with
        the cat serialized in it.
        """

        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lostcats/cat_detail.html")
        self.assertEqual(resp.context["cat"], self.cat)
        self.assertEqual(resp.context["json_data"], cat_serializer(self.cat))
        self.assertContains(
            resp,
            text=self.client.json_encoder().encode(cat_serializer(self.cat)),
            count=1,
        )
        self.assertContains(
            resp,
            text=f"<title>{self.cat.title} | LostCat Ithaca</title>",
            count=1,
        )

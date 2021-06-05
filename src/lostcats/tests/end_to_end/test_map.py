from django.urls import reverse

from lostcats.tests.utils import TemporaryMediaTestCase
from lostcats.tests.factories import LostCatFactory
from lostcats.models import LostCat
from lostcats.serializers import cat_serializer


class TestMap(TemporaryMediaTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("map")

    def test_fetch_no_cats(self):
        """The map should be rendered with 200 OK."""
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lostcats/map.html")
        self.assertQuerysetEqual(resp.context["cats"], LostCat.objects.none())
        self.assertEqual(resp.context["json_data"], [])

    def test_fetch(self):
        """The map should be rendered with 200 OK and all cats in
        JSON script.
        """
        LostCatFactory.create_batch(20)
        cats = LostCat.objects.all()

        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(resp.context["cats"], cats)
        self.assertEqual(
            resp.context["json_data"], [cat_serializer(cat) for cat in cats]
        )

        for cat in cats:
            self.assertContains(
                resp,
                text=self.client.json_encoder().encode(cat_serializer(cat)),
                count=1,
            )

    def test_page_title(self):
        """The page title should be "Map | LostCat Ithaca"."""
        resp = self.client.get(self.url)

        self.assertContains(resp, "<title>Map | LostCat Ithaca</title>", count=1)

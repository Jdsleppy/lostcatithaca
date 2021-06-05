from django.urls import reverse
from django.core.paginator import Page

from lostcats.tests.utils import TemporaryMediaTestCase
from lostcats.tests.factories import LostCatFactory
from lostcats.models import LostCat


class TestGallery(TemporaryMediaTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("gallery")

    def test_fetch_many_pages(self):
        """Test happy path pagination."""
        LostCatFactory.create_batch(24)
        resp = self.client.get(self.url, {"page": 1})
        self.assertQuerysetEqual(resp.context["cats"], LostCat.objects.all()[:10])

        page = resp.context["page_obj"]  # type: Page
        self.assertTrue(page.has_other_pages())
        self.assertFalse(page.has_previous())
        self.assertTrue(page.has_next())
        self.assertEqual(page.number, 1)

        resp = self.client.get(self.url, {"page": 2})
        self.assertQuerysetEqual(resp.context["cats"], LostCat.objects.all()[10:20])

        page = resp.context["page_obj"]  # type: Page
        self.assertTrue(page.has_other_pages())
        self.assertTrue(page.has_previous())
        self.assertTrue(page.has_next())
        self.assertEqual(page.number, 2)

        resp = self.client.get(self.url, {"page": 3})
        self.assertQuerysetEqual(resp.context["cats"], LostCat.objects.all()[20:24])

        page = resp.context["page_obj"]  # type: Page
        self.assertTrue(page.has_other_pages())
        self.assertTrue(page.has_previous())
        self.assertFalse(page.has_next())
        self.assertEqual(page.number, 3)

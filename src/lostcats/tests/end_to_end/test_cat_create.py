from io import BytesIO

from django.urls import reverse

from lostcats.tests.utils import TemporaryMediaTestCase, IMAGES_DIR
from lostcats.models import LostCat


class TestCatCreate(TemporaryMediaTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("cat-create")

    def test_get_no_coords_invalid_request(self):
        """If query params don't include latitude and longitude,
        return a 400.
        """
        resp = self.client.get(self.url)

        self.assertEqual(resp.status_code, 400)
        self.assertTemplateNotUsed(resp, "lostcats/cat_create.html")

    def test_get_creates_form_with_initial_coords(self):
        """After a GET when query params, the coords from the query params
        should be set as the form's initial values.
        """
        latitude = 74.783
        longitude = -42.999

        resp = self.client.get(self.url, {"latitude": latitude, "longitude": longitude})

        self.assertEqual(resp.context["form"].initial["latitude"], str(latitude))
        self.assertEqual(resp.context["form"].initial["longitude"], str(longitude))

    def test_get_renders_json_script_with_initial_coords(self):
        """After a GET when query params, the coords from the query params
        should be rendered as a JSON script for consumption by JS.
        """
        latitude = "74.783"
        longitude = "-42.999"

        coords_dict = {
            "latitude": latitude,
            "longitude": longitude,
        }

        resp = self.client.get(self.url, coords_dict)

        self.assertEqual(resp.context["json_data"], coords_dict)
        self.assertContains(
            resp,
            self.client.json_encoder().encode(coords_dict),
        )

    def test_post_new_cat(self):
        """A happy path POST should create a new cat and redirect to that
        cat's detail page.
        """
        with (IMAGES_DIR / "cat1.png").open("rb") as f:
            img_data = BytesIO(f.read())
            img_data.name = "cat1.png"

        post_data = {
            "title": "A Cat Darkly",
            "description": "A cat noir, ooh ooh spooky spooky!",
            "image": img_data,
            "latitude": 123.4567,
            "longitude": -98.7654,
        }
        resp = self.client.post(
            self.url,
            data=post_data,
        )

        cat = LostCat.objects.get()
        self.assertEqual(cat.title, post_data["title"])
        self.assertEqual(cat.description, post_data["description"])
        self.assertEqual(cat.latitude, post_data["latitude"])
        self.assertEqual(cat.longitude, post_data["longitude"])

        self.assertRedirects(resp, cat.get_absolute_url())

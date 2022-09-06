from lostcats.tests.utils import TemporaryMediaTestCase
from lostcats.tests.factories import LostCatFactory


class TestLostCat(TemporaryMediaTestCase):
    def test_small_image_not_resized(self):
        cat = LostCatFactory(image__width=150, image__height=180)

        self.assertEqual(cat.image.width, 150)
        self.assertEqual(cat.image.height, 180)

        self.assertEqual(cat.resized_image.width, 150)
        self.assertEqual(cat.resized_image.height, 180)

        self.assertEqual(cat.thumbnail.width, 150)
        self.assertEqual(cat.thumbnail.height, 180)

    def test_medium_image_is_thumbnailed(self):
        cat = LostCatFactory(image__width=500, image__height=600)

        self.assertEqual(cat.image.width, 500)
        self.assertEqual(cat.image.height, 600)

        self.assertEqual(cat.resized_image.width, 500)
        self.assertEqual(cat.resized_image.height, 600)

        self.assertEqual(cat.thumbnail.width, 200)
        self.assertEqual(cat.thumbnail.height, 240)

    def test_large_image_is_thumbnailed_and_resized(self):
        cat = LostCatFactory(image__width=1500, image__height=1600)

        self.assertEqual(cat.image.width, 1500)
        self.assertEqual(cat.image.height, 1600)

        self.assertEqual(cat.resized_image.width, 750)
        self.assertEqual(cat.resized_image.height, 800)

        self.assertEqual(cat.thumbnail.width, 200)
        self.assertEqual(cat.thumbnail.height, 213)

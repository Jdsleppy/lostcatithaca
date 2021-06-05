import pathlib
import shutil

from django import test

TESTS_DIR = pathlib.Path(__file__).resolve().parent
IMAGES_DIR = TESTS_DIR / "images"
TEST_MEDIA_DIR = TESTS_DIR / "test_media_dir"


@test.override_settings(MEDIA_DIR=str(TEST_MEDIA_DIR))
class TemporaryMediaTestCase(test.TestCase):
    def setUp(self):
        TEST_MEDIA_DIR.mkdir(exist_ok=True)

    def tearDown(self) -> None:
        shutil.rmtree(TEST_MEDIA_DIR)
        super().tearDown()

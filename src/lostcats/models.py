import io
import pathlib

from django.core.exceptions import ValidationError
from django.core import files
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse

from PIL import Image, ImageOps
from model_utils import FieldTracker


def validate_coordinate_global_limit(coord):
    if coord < -180 or coord > 180:
        raise ValidationError(
            _("%(value)s is not within -180 to 180 degrees"),
            params={"value": coord},
        )


def lost_cat_image_path(lostcat, filename):
    return f"uploads/{slugify(lostcat.title)}_{filename}"


class LostCat(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=500)
    latitude = models.FloatField(validators=[validate_coordinate_global_limit])
    longitude = models.FloatField(validators=[validate_coordinate_global_limit])
    image = models.ImageField(upload_to=lost_cat_image_path)
    resized_image = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tracker = FieldTracker(fields=["image", "title"])

    class Meta:
        ordering = [
            "-created",
        ]

    def __str__(self) -> str:
        return f"{self.pk}: {self.title}"

    def get_absolute_url(self):
        return reverse("cat-detail", kwargs={"pk": self.pk, "slug": self.slug})

    @property
    def image_url(self) -> str:
        if not self.image:
            return ""

        return self.image.url

    @property
    def resized_image_url(self) -> str:
        if not self.resized_image:
            return ""

        return self.resized_image.url

    @property
    def thumbnail_url(self) -> str:
        if not self.thumbnail:
            return ""

        return self.thumbnail.url

    def generate_thumbnails(self) -> None:
        if not self.image:
            raise ValueError(
                "Cannot generate thumbnails because the original image is not present."
            )

        full_image_path = pathlib.Path(self.image.path)
        image_extension = full_image_path.suffix
        thumbnail_name = self.image.name.replace(
            image_extension, f"_thumbnail{image_extension}"
        )
        resized_image_name = self.image.name.replace(
            image_extension, f"_resized{image_extension}"
        )

        # One at a time to avoid high memory consumption

        # thumbnail
        with Image.open(self.image) as pil_image:

            pil_image.thumbnail((200, 300))

            # Convert from PIL image to Django image
            thumbnail_buffer = io.BytesIO()
            pil_image.save(thumbnail_buffer, pil_image.format)

        # resized_image
        with Image.open(self.image) as pil_image:

            pil_image.thumbnail((750, 1500))

            # Convert from PIL image to Django image
            resized_image_buffer = io.BytesIO()
            pil_image.save(resized_image_buffer, pil_image.format)

        with files.File(thumbnail_buffer) as django_file:
            self.thumbnail.save(thumbnail_name, django_file, save=False)

        with files.File(resized_image_buffer) as django_file:
            self.resized_image.save(resized_image_name, django_file, save=False)

    def strip_exif_data(self) -> None:
        """Strip image exif data.

        This is good for privacy, and also prevents undesired rotations when rendered
        in browsers.

        Only call this from .save()!
        """
        with Image.open(self.image) as original_image:
            transposed = ImageOps.exif_transpose(original_image)

            # # create output image, forgetting the EXIF metadata
            # stripped = Image.new(original.mode, original.size)
            # stripped.putdata(list(original.getdata()))

            # Convert from PIL image to Django image
            file_buffer = io.BytesIO()
            transposed.save(file_buffer, format=original_image.format)

        with files.File(file_buffer) as django_file:
            self.image.save(
                self.image.name,
                django_file,
                # doesn't save the model changes, so should only be called from .save()!
                save=False,
            )

    def save(self, *args, **kwargs) -> None:
        if self.tracker.has_changed("image"):
            self.strip_exif_data()
            self.generate_thumbnails()

        if self.tracker.has_changed("title"):
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

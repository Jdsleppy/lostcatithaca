from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


def validate_coordinate_global_limit(coord):
    if coord < -180 or coord > 180:
        raise ValidationError(
            _("%(value)s is not within -180 to 180 degrees"),
            params={"value": coord},
        )


def lost_cat_image_path(lostcat, filename):
    return f'uploads/{str(lostcat.latitude).replace("-", "S").replace(".", "-")}_{str(lostcat.longitude).replace("-", "W").replace(".", "-")}_{filename}'


class LostCat(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField(validators=[validate_coordinate_global_limit])
    longitude = models.FloatField(validators=[validate_coordinate_global_limit])
    image = models.ImageField(upload_to=lost_cat_image_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "-updated",
        ]

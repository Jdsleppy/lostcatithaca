from typing import Any, Dict

from lostcats.models import LostCat


def cat_serializer(cat: LostCat) -> Dict[str, Any]:
    """Converts to dict for presentation to Javascript code as a JSON script."""
    return {
        "url": cat.get_absolute_url(),
        "image_url": cat.image_url,
        "resized_image_url": cat.resized_image_url,
        "thumbnail_url": cat.thumbnail_url,
        "title": cat.title,
        "description": cat.description,
        "latitude": cat.latitude,
        "longitude": cat.longitude,
    }

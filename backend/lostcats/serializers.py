from rest_framework import serializers

from .models import LostCat


class LostCatSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField()

    class Meta:
        model = LostCat
        fields = [
            "id",
            "description",
            "latitude",
            "longitude",
            "image_url",
            "created",
            "updated",
        ]
        read_only_fields = [
            "id",
            "created",
            "updated",
        ]

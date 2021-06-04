from rest_framework import mixins, viewsets

from .models import LostCat
from .serializers import LostCatSerializer


class LostCatViewset(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = LostCatSerializer
    queryset = LostCat.objects.all()

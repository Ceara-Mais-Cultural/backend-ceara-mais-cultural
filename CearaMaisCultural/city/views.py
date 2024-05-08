from .models import City
from rest_framework import permissions, viewsets
from rest_framework import mixins

from .serializers import CitySerializer


class CityViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows cities to be viewed.
    """

    queryset = City.objects.all().order_by("name")
    serializer_class = CitySerializer
    # permission_classes = [permissions.IsAuthenticated]

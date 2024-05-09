from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .serializers import CitySerializer
from .models import City


class CityViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows cities to be viewed.
    """

    queryset = City.objects.all().order_by("name")
    serializer_class = CitySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]

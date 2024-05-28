from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .serializers import NeighborhoodSerializer
from .models import Neighborhood


class NeighborhoodViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows neighborhoods to be viewed.
    """

    queryset = Neighborhood.objects.all().order_by("id")
    serializer_class = NeighborhoodSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
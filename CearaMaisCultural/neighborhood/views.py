from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .serializers import NeighborhoodSerializer
from .models import Neighborhood
from CearaMaisCultural.permissions import IsAdminOrReadOnly


class NeighborhoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows neighborhoods to be viewed.
    """

    queryset = Neighborhood.objects.all().order_by("id")
    serializer_class = NeighborhoodSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

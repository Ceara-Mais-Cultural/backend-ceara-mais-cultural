from rest_framework import viewsets, mixins, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from neighborhood.serializers import NeighborhoodSerializer
from neighborhood.models import Neighborhood

from .serializers import CitySerializer
from .models import City


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed.
    """

    queryset = City.objects.all().order_by("id")
    serializer_class = CitySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    @action(detail=True, methods=["get"])
    def neighborhoods(self, _, pk=None):
        city = get_object_or_404(City, pk=pk)
        neighborhoods = Neighborhood.objects.filter(city=city)
        serializer = NeighborhoodSerializer(neighborhoods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

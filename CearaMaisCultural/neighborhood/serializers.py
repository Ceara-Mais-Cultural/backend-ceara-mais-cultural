from .models import Neighborhood
from rest_framework import serializers


class NeighborhoodSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = Neighborhood
        fields = ["id", "name", "city", "city_name"]

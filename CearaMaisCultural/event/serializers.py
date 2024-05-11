from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    project_title = serializers.CharField(source="project.title", read_only=True)
    city_name = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = Event
        fields = ["id", "name", "project", "project_title", "city", "city_name"]

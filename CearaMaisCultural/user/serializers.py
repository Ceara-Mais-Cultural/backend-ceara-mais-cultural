from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="city.name", read_only=True)
    neighborhood_name = serializers.CharField(
        source="neighborhood.name", read_only=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "cpf",
            "full_name",
            "email",
            "city",
            "city_name",
            "neighborhood",
            "neighborhood_name",
            "community",
            "is_staff",
            "is_superuser",
            "date_joined",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

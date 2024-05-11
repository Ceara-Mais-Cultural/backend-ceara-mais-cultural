from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "cpf",
            "full_name",
            "email",
            "city",
            "city_name",
            "is_staff",
            "date_joined",
        )

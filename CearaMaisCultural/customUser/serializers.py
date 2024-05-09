from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source="city.name", read_only=True)

    class Meta:
        model = CustomUser
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

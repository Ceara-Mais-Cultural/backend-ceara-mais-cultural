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
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class DeleteUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

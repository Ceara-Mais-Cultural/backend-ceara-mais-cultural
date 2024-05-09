from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.full_name", read_only=True)
    promoter_name = serializers.CharField(source="promoter.full_name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "location",
            'category',
            "category_name",
            "created_at",
            'author',
            "author_name",
            'promoter',
            "promoter_name",
        ]

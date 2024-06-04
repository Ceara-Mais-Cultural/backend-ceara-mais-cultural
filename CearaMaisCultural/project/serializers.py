from .models import Project, ProjectVote
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.full_name", read_only=True)
    promoter_name = serializers.CharField(source="promoter.full_name", read_only=True)
    city_name = serializers.CharField(
        source="city.name", read_only=True
    )
    neighborhood_name = serializers.CharField(
        source="neighborhood.name", read_only=True
    )
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            'city',
            'city_name',
            'neighborhood',
            'neighborhood_name',
            'community',
            "location",
            "category",
            "category_name",
            "created_at",
            "author",
            "author_name",
            "promoter",
            "promoter_name",
            "status"
        ]

class ProjectVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectVote
        fields = '__all__'
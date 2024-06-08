import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    community = django_filters.CharFilter(field_name='community', lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['title', 'category', 'city', 'neighborhood', 'community', 'author', 'promoter']

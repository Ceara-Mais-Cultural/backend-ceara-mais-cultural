from .models import Document
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):
    project_title = serializers.CharField(source="project.title", read_only=True)
    
    class Meta:
        model = Document
        fields = ['id', 'file', 'name', 'project', 'project_title']
from .models import Document
from rest_framework import permissions, viewsets

from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = Document.objects.all().order_by('name')
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
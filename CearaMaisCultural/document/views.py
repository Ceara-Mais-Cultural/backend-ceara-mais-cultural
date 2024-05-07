from .models import Document
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from django.http import FileResponse

from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["get"])
    def view(self, request, pk=None):
        document = self.get_object()
        # Assuming 'file' is the field containing the image file
        return FileResponse(document.file)

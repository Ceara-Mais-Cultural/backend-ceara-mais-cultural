from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.http import FileResponse

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["get"])
    def view(self, request, pk=None):
        document = self.get_object()
        return FileResponse(document.file)

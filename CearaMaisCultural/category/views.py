from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    API endpoint that allows categories to be viewed.
    """

    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

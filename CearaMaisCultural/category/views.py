from rest_framework import viewsets, permissions

from .models import Category
from .serializers import CategorySerializer
from CearaMaisCultural.permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """

    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated]
    
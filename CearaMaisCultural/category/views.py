from rest_framework import viewsets
from rest_framework import mixins
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    A viewset that provides only retrieval and listing of categories.
    """

    queryset = Category.objects.all()  # Defina o queryset aqui
    serializer_class = CategorySerializer

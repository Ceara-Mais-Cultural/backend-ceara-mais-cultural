from .models import CustomUser
from rest_framework import permissions, viewsets

from .serializers import CustomUserSerializer


class  CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('first_name')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
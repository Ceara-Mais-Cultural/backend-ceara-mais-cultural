from .models import CustomUser
from rest_framework import permissions, viewsets

from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('is_staff')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
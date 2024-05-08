from .models import CustomUser
from rest_framework import permissions, viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = CustomUser.objects.all().order_by("is_staff")
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        password = self.request.data.get("password")
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

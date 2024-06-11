from django.forms import ValidationError
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import User
from .serializers import DeleteUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["city", "is_staff", "is_superuser"]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            password = self.request.data.get("password")
            hashed_password = make_password(password)
            user = serializer.save(password=hashed_password)
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "user": UserSerializer(user).data},
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
def loginView(request):
    user = get_object_or_404(User, email=request.data["email"])
    if user.check_password(request.data["password"]):
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteUserView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'delete_user_form.html')

    def post(self, request, *args, **kwargs):
        serializer = DeleteUserSerializer(data=request.POST)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(username=email, password=password)
            if user:
                user.delete()
                return render(request, 'delete_user_form.html', {"message": "Usuário excluído com sucesso."})
            else:
                return render(request, 'delete_user_form.html', {"error": "Credenciais inválidas."})
        return render(request, 'delete_user_form.html', {"errors": serializer.errors})

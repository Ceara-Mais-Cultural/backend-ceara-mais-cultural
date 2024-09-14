from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    Permissão que permite leitura a qualquer usuário autenticado, mas só permite escrita a usuários admin.
    """

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return request.user and request.user.is_staff


class IsAuthenticatedOrCreate(BasePermission):
    """
    Permissão que permite criação de novos usuários sem autenticação,
    mas exige autenticação para recuperação, edição e exclusão.
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return True

        return request.user and request.user.is_authenticated
    
class IsAdminUser(BasePermission):
    """
    Permissão que permite acesso apenas para usuários administradores.
    """
    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado e se é um administrador
        return request.user and request.user.is_authenticated and request.user.is_staff and request.user.is_superuser

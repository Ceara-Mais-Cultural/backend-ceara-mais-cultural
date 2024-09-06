from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

from project.views import ProjectViewSet, ProjectVoteViewSet
from city.views import CityViewSet
from neighborhood.views import NeighborhoodViewSet
from category.views import CategoryViewSet
from user.views import DeleteUserView, UserViewSet, loginView, ConfirmIdentityView, ResetPasswordView, ResetSuccessfulView, UserDeletedView
from .views import privacy_policy_view

admin.site.site_title = "Ceará Mais Cultural"
admin.site.site_header = "Administração"

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"projects-votes", ProjectVoteViewSet)
router.register(r"cities", CityViewSet)
router.register(r"neighborhoods", NeighborhoodViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", loginView),
    path("admin/", admin.site.urls),
    path("excluir-conta/", DeleteUserView.as_view(), name="delete_user"),
    path("politica-privacidade/", privacy_policy_view, name="privacy_policy"),
    path('confirmar-identidade/', ConfirmIdentityView.as_view(), name='confirm_identity'),
    path('redefinir-senha/<str:token>/', ResetPasswordView.as_view(), name='reset_password'),
    path('senha-redefinida/', ResetSuccessfulView.as_view(), name='reset_successful'),
    path('usuario-excluido/', UserDeletedView.as_view(), name='user_DELETED'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

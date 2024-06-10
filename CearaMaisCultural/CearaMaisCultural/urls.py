from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

from project.views import ProjectViewSet, ProjectVoteViewSet
from city.views import CityViewSet
from neighborhood.views import NeighborhoodViewSet
from category.views import CategoryViewSet
from user.views import UserViewSet, loginView

admin.site.site_title = "Ceará Mais Cultural - Adm (DEV)"
admin.site.site_header = "Ceará mais Cultural - Administração"

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
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("ceara-admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

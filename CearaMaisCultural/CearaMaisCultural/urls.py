from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from project.views import ProjectViewSet
from city.views import CityViewSet
from neighborhood.views import NeighborhoodViewSet
from document.views import DocumentViewSet
from category.views import CategoryViewSet
from user.views import UserViewSet, login

admin.site.site_title = "Ceará Mais Cultural - Adm (DEV)"
admin.site.site_header = "Ceará mais Cultural - Administração"

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"cities", CityViewSet)
router.register(r"neighborhoods", NeighborhoodViewSet)
router.register(r"documents", DocumentViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login', login),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('ceara-admin/', admin.site.urls),
]

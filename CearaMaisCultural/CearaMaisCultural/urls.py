from django.urls import include, path
from rest_framework import routers

from project.views import ProjectViewSet
from city.views import CityViewSet
from document.views import DocumentViewSet
from category.views import CategoryViewSet
from customUser.views import signup, login, get_users

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"cities", CityViewSet)
router.register(r"documents", DocumentViewSet)
router.register(r"categories", CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path('signup', signup),
    path('login', login),
    path('users', get_users),
]

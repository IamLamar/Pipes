from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import NewsViewSet

router = DefaultRouter()
router.register(r"", NewsViewSet, basename="news")

urlpatterns = [
    path("", include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import BannerSingleView, ClientsViewSet, VideoSectionViewSet, GratitudeSectionViewSet

router = DefaultRouter()
router.register(r"video", VideoSectionViewSet, basename="video-sections")
router.register(r"gratitude", GratitudeSectionViewSet, basename="gratitude-sections")
router.register(r"clients", ClientsViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls)),
    path("banner/", BannerSingleView.as_view(), name="banner-single"),

]

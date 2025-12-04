from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer, ProjectShortSerializer


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectShortSerializer

    def get_queryset(self): # pyright: ignore[reportIncompatibleMethodOverride]
        return Project.objects.select_related("category")


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    lookup_field = "pk"

    def get_queryset(self): # pyright: ignore[reportIncompatibleMethodOverride]
        return Project.objects.select_related("category").prefetch_related("galleries")

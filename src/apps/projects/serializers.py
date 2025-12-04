from rest_framework import serializers

from common.serializers import AbsoluteImageUrlMixin
from .models import Category, Project, ProjectGallery

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProjectGallerySerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):

    class Meta:
        model = ProjectGallery
        fields = ["id", "image"]


class ProjectSerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):
    galleries = ProjectGallerySerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id", "name", "address", "title", "company",
            "term", "task", "solution", "gratitude", "galleries"
        )

class ProjectShortSerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Project
        fields = ('id', 'category', 'company', 'image', 'name', 'address')

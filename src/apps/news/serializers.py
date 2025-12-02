from rest_framework import serializers

from common.serializers import AbsoluteImageUrlMixin
from .models import Category, News

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class NewsSerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'reading_time', 'content_title', 'description', 'image')


class NewsShortSerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = News
        fields = ('id', 'category', 'title', 'image', 'created_at')

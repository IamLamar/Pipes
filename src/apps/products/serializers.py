from rest_framework import serializers

from common.serializers import AbsoluteImageUrlMixin
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'image', 'name', 'price')

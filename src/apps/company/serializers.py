from rest_framework import serializers
from .models import CompanyBanner, CompanyInNumbers, CompanyValue, Experts


class CompanyBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBanner
        fields = ('id', 'title', 'description' , 'image', 'video')


class CompanyInNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInNumbers
        fields = ('id', 'number', 'description')


class CompanyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyValue
        fields = ('id', 'field_of_activivty', 'mission', 'values', 'description', 'image')


class ExpertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experts
        fields = ('id', 'name', 'photo', 'experience', 'position')

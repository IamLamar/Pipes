from rest_framework import serializers
from .models import CompanyBanner, CompanyInNumbers, CompanyValue, Documents, Experts, CompanyPhoto


class CompanyBannerSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = CompanyBanner
        fields = ('id', 'title', 'description', 'image', 'video')

    def get_video(self, obj):
        # Возвращаем первый непустой источник видео
        if obj.video_url:
            return obj.video_url.url if hasattr(obj.video_url, 'url') else obj.video_url
        if obj.video_file:
            return obj.video_file.url if hasattr(obj.video_file, 'url') else obj.video_file
        return None

    def validate(self, attrs):
        video_url = attrs.get('video_url')
        video_file = attrs.get('video_file')

        if not video_url and not video_file:
            raise serializers.ValidationError("Нужно указать ссылку на видео или загрузить файл.")
        if video_url and video_file:
            raise serializers.ValidationError("Можно указать только одно: ссылку или файл.")
        return attrs


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


class CompanyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPhoto
        fields = ('id', 'image')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('id', 'title', 'description', 'file_url')

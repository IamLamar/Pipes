from rest_framework import serializers
from .models import Banner, Clients, VideoSection, GratitudeSection


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("id", "image", "title", "description")

class VideoSectionSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = VideoSection
        fields = ("id", "title", "description", "date", "video")

    def get_video(self, obj):
        """Возвращает ссылку на видео: локальный файл или URL"""
        request = self.context.get("request")
        if obj.video_file:
            if request:
                return request.build_absolute_uri(obj.video_file.url)
            return obj.video_file.url
        return obj.video_url


class GratitudeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GratitudeSection
        fields = ("id", "image")


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ("id", "title", "description", "image")

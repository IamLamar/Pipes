from rest_framework import serializers
from .models import Banner, Clients, VideoSection, GratitudeSection


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("id", "image", "title", "description")

class VideoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSection
        fields = ("id", "video_url", "title", "description", "date")


class GratitudeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GratitudeSection
        fields = ("id", "image")


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ("id", "title", "description", "image")

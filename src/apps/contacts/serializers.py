from rest_framework import serializers

from common.serializers import AbsoluteImageUrlMixin
from .models import Contact, AcceptancePerson


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'address', 'phone_number', 'email', 'working_hours', 'whatsapp_number', 'telegram_number', 'instagram', 'facebook')


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    comment = serializers.CharField()


class AcceptancePersonSerializer(AbsoluteImageUrlMixin, serializers.ModelSerializer):
    class Meta:
        model = AcceptancePerson
        fields = ('id', 'full_name', 'position', 'photo')

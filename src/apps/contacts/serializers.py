from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'address', 'phone_number', 'email', 'working_hours', 'whatsapp_number', 'telegram_number', 'instagram', 'facebook')


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    comment = serializers.CharField()

from django.db import models
from common.model import BaseModel


class Contact(BaseModel):
    working_hours = models.CharField(max_length=100, verbose_name="Рабочие часы")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    whatsapp_number = models.CharField(max_length=20, verbose_name="Номер WhatsApp")
    telegram_number = models.CharField(max_length=20, verbose_name="Номер Telegram")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    instagram = models.URLField(verbose_name="Ссылка на Instagram")
    facebook = models.URLField(verbose_name="Ссылка на Facebook")

    class Meta(BaseModel.Meta):
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.phone_number} - {self.email}"

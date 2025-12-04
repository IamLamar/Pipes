from django.db import models
from common.model import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class Service(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    schedule = models.CharField(max_length=255, verbose_name="График работы")
    phone = PhoneNumberField(verbose_name="Номер телефона", max_length=20)

    class Meta(BaseModel.Meta):
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self) -> str:
        return self.title

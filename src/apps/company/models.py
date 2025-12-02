from django.db import models

from common.model import BaseModel


class CompanyBanner(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='company_banners/')
    video = models.FileField(upload_to='company_videos/', null=True, blank=True)

    class Meta(BaseModel.Meta):
        verbose_name = "Баннер компании"
        verbose_name_plural = "Баннер компании"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class CompanyInNumbers(BaseModel):
    number = models.CharField(max_length=10, verbose_name="Число")
    description = models.CharField(max_length=50, verbose_name="Описание")

    class Meta(BaseModel.Meta):
        verbose_name = "Компания в цифрах"
        verbose_name_plural = "Компания в цифрах"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.number} - {self.description}"


class CompanyValue(BaseModel):
    field_of_activivty = models.TextField(max_length=255, verbose_name="Сфера деятельности")
    mission = models.TextField(max_length=255, verbose_name="Миссия")
    values = models.TextField(max_length=255, verbose_name="Ценности")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='company_values/', verbose_name="Изображение")

    class Meta(BaseModel.Meta):
        verbose_name = "Ценности компании"
        verbose_name_plural = "Ценности компании"
        ordering = ['-created_at']


class Experts(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Имя")
    photo = models.ImageField(upload_to='experts_photos/', verbose_name="Фото")
    experience = models.CharField(max_length=50, verbose_name="Опыт")
    position = models.CharField(max_length=100, verbose_name="Должность")

    class Meta(BaseModel.Meta):
        verbose_name = "Эксперт"
        verbose_name_plural = "Эксперты"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

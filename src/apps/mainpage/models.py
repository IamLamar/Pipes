from django.db import models
from common.model import BaseModel


class Banner(BaseModel):
    image = models.ImageField(upload_to="banners/", verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", max_length=200)

    class Meta(BaseModel.Meta):
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class VideoSection(BaseModel):
    video_url = models.URLField(verbose_name="URL видео")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", max_length=100)
    date = models.CharField(max_length=100, verbose_name="Дата")

    class Meta(BaseModel.Meta):
        verbose_name = "Видео секция"
        verbose_name_plural = "Видео секции"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class GratitudeSection(BaseModel):
    image = models.ImageField(upload_to="gratitude/", verbose_name="Изображение")

    class Meta(BaseModel.Meta):
        verbose_name = "Секция благодарности"
        verbose_name_plural = "Секции благодарности"
        ordering = ['-created_at']


class Clients(BaseModel):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", max_length=20)
    image = models.ImageField(upload_to="clients/", verbose_name="Изображение")

    class Meta(BaseModel.Meta):
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

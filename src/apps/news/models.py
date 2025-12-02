from django.db import models
from common.model import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta(BaseModel.Meta):
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class News(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news", verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    reading_time = models.CharField(max_length=50, verbose_name="Время чтения")
    content_title = models.TextField(verbose_name="Содержание")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="news/", verbose_name="Изображение")

    class Meta(BaseModel.Meta):
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

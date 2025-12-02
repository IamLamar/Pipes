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


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение")
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.CharField(max_length=20, verbose_name="Цена")

    class Meta(BaseModel.Meta):
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

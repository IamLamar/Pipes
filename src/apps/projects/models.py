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


class Project(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="projects", verbose_name="Категория")
    name  = models.CharField(max_length=100, verbose_name="Название проекта")
    address = models.CharField(max_length=20, verbose_name="Адрес")
    company = models.CharField(max_length=100, verbose_name="Компания")
    term = models.CharField(max_length=50, verbose_name="Сроки")
    image = models.ImageField(upload_to="projects/", verbose_name="Изображение")
    title = models.CharField(max_length=255, verbose_name="Описание объекта")
    task = models.TextField(verbose_name="Задача")
    solution = models.TextField(verbose_name="Решение")
    gratitude = models.TextField(verbose_name="Благодарность")


    class Meta(BaseModel.Meta):
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProjectGallery(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="galleries", verbose_name="Проект")
    image = models.ImageField(upload_to="projects/", verbose_name="Изображение")

    class Meta(BaseModel.Meta):
        verbose_name = "Галерея проекта"
        verbose_name_plural = "Галерея проекта"
        ordering = ['-created_at']

    def __str__(self):
        return f"Галерея проекта {self.project.name}"

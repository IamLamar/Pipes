from django.contrib import admin

from apps.projects.models import Project, ProjectGallery, Category


class GalleryProjectInline(admin.TabularInline):
    model = ProjectGallery
    min_num = 5
    fields = ("image",)

class ProjectAdmin(admin.ModelAdmin):
    inlines = [GalleryProjectInline]

admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)

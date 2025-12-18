from django.contrib import admin
from .models import CompanyBanner, CompanyInNumbers, CompanyPhoto, CompanyValue, Documents, Experts


@admin.register(CompanyBanner)
class CompanyBannerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title', 'description', 'image', 'video_url', 'video_file')

    def has_add_permission(self, request):
        # Разрешаем добавлять только если нет ни одного объекта
        return not self.model.objects.exists()

    def save_model(self, request, obj, form, change):
        # Вызываем clean перед сохранением
        obj.clean()
        super().save_model(request, obj, form, change)


admin.site.register(CompanyInNumbers)
admin.site.register(CompanyValue)
admin.site.register(Experts)
admin.site.register(CompanyPhoto)
admin.site.register(Documents)

from django.contrib import admin
from .models import Banner, VideoSection, GratitudeSection, Clients
from django.utils.html import format_html


@admin.register(VideoSection)
class VideoSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "video_preview")
    readonly_fields = ("video_preview",)

    fieldsets = (
        (None, {
            "fields": ("title", "description", "date", "video_url", "video_file", "video_preview")
        }),
    )

    def video_preview(self, obj):
        """Показывает превью видео в админке, если есть"""
        if obj.video_file:
            return format_html(
                '<video width="320" height="240" controls>'
                '<source src="{}" type="video/mp4">'
                'Ваш браузер не поддерживает видео.'
                '</video>',
                obj.video_file.url
            )
        elif obj.video_url:
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                obj.video_url,
                "Ссылка на видео"
            )
        return "-"
    video_preview.short_description = "Видео"


admin.site.register(GratitudeSection)
admin.site.register(Clients)

class BannerAdmin(admin.ModelAdmin):
    redirect_on_change = True

    def has_add_permission(self, request):
        return not self.model.objects.exists()

admin.site.register(Banner, BannerAdmin)

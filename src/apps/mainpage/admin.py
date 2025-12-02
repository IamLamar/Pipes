from django.contrib import admin
from .models import Banner, VideoSection, GratitudeSection, Clients

admin.site.register(VideoSection)
admin.site.register(GratitudeSection)
admin.site.register(Clients)

class BannerAdmin(admin.ModelAdmin):
    redirect_on_change = True

    def has_add_permission(self, request):
        return not self.model.objects.exists()

admin.site.register(Banner, BannerAdmin)

from django.contrib import admin
from .models import CompanyBanner, CompanyInNumbers, CompanyValue, Experts

class CompanyBannerAdmin(admin.ModelAdmin):
    redirect_on_change = True

    def has_add_permission(self, request):
        return not self.model.objects.exists()

admin.site.register(CompanyBanner, CompanyBannerAdmin)

admin.site.register(CompanyInNumbers)
admin.site.register(CompanyValue)
admin.site.register(Experts)

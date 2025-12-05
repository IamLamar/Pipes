from django.contrib import admin
from .models import AcceptancePerson, Contact

class ContactAdmin(admin.ModelAdmin):
    redirect_on_change = True

    def has_add_permission(self, request):
        return not self.model.objects.exists()

admin.site.register(Contact, ContactAdmin)

class AcceptancePersonAdmin(admin.ModelAdmin):
    redirect_on_change = True

    def has_add_permission(self, request):
        return not self.model.objects.exists()

admin.site.register(AcceptancePerson, AcceptancePersonAdmin)

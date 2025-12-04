from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from django.http import HttpResponse
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.static import serve


def health_check(request):
    return HttpResponse("OK")


urlpatterns = [
    path("", health_check),
    path("admin/", admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path("api/v1/mainpage/", include("apps.mainpage.urls")),
    path("api/v1/products/", include("apps.products.urls")),
    path("api/v1/news/", include("apps.news.urls")),
    path("api/v1/contacts/", include("apps.contacts.urls")),
    path("api/v1/company/", include("apps.company.urls")),
    path("api/v1/services/", include("apps.service_page.urls")),
    path("api/v1/projects/", include("apps.projects.urls")),
    re_path(r'^back_media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),

]

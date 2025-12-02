from rest_framework.viewsets import ReadOnlyModelViewSet

from common.pagination import Pagination
from .models import News
from .serializers import NewsSerializer, NewsShortSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(summary="Получить список новостей"),
    retrieve=extend_schema(summary="Получить детали новости по ID")
)
class NewsViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.all()

    def get_serializer_class(self): # type: ignore
        if self.action == "list":
            return NewsShortSerializer
        return NewsSerializer
    pagination_class = Pagination

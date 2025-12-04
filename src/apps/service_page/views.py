from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Service
from .serializers import ServiceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    retrieve=extend_schema(exclude=True)
)
class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

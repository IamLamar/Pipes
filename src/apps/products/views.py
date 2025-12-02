from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    retrieve=extend_schema(exclude=True)
)
class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema_view(
    retrieve=extend_schema(exclude=True)
)
class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

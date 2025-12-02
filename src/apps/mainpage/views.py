from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Banner, VideoSection, GratitudeSection, Clients
from .serializers import BannerSerializer, ClientsSerializer, VideoSectionSerializer, GratitudeSectionSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


class BannerSingleView(APIView):
    serializer_class = BannerSerializer

    def get(self, request):
        obj = Banner.objects.last()
        serializer =BannerSerializer(obj, context={'request': request})
        return Response(serializer.data if obj else None)


@extend_schema_view(
    retrieve=extend_schema(exclude=True)
)
class VideoSectionViewSet(ReadOnlyModelViewSet):
    queryset = VideoSection.objects.all()
    serializer_class = VideoSectionSerializer

@extend_schema_view(
    retrieve=extend_schema(exclude=True)
)
class GratitudeSectionViewSet(ReadOnlyModelViewSet):
    queryset = GratitudeSection.objects.all()
    serializer_class = GratitudeSectionSerializer


@extend_schema_view(
    retrieve=extend_schema(exclude=True)
)
class ClientsViewSet(ReadOnlyModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

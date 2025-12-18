from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import CompanyBanner, CompanyInNumbers, CompanyValue, Documents, Experts, CompanyPhoto
from .serializers import CompanyBannerSerializer, CompanyInNumbersSerializer, CompanyPhotoSerializer, CompanyValueSerializer, DocumentSerializer, ExpertsSerializer
# from drf_spectacular.utils import extend_schema, extend_schema_view

class CompanyBannerSingleView(APIView):
    serializer_class = CompanyBannerSerializer

    def get(self, request):
        obj = CompanyBanner.objects.last()
        serializer =CompanyBannerSerializer(obj, context={'request': request})
        return Response(serializer.data if obj else None)


class CompanyInNumbersListView(ListAPIView):
    queryset = CompanyInNumbers.objects.all()
    serializer_class = CompanyInNumbersSerializer


class CompanyValueListView(ListAPIView):
    queryset = CompanyValue.objects.all()
    serializer_class = CompanyValueSerializer


class ExpertsListView(ListAPIView):
    queryset = Experts.objects.all()
    serializer_class = ExpertsSerializer


class CompanyPhotoView(APIView):
    serializer_class = CompanyPhotoSerializer

    def get(self, request):
        obj = CompanyPhoto.objects.last()
        serializer =CompanyPhotoSerializer(obj, context={'request': request})
        return Response(serializer.data if obj else None)


class DocumentsListView(ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer

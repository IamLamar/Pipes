from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from threading import Thread
from .models import Contact
from .serializers import ContactSerializer, FeedbackSerializer
from .services import send_feedback_email


class ContactSingleView(APIView):
    serializer_class = ContactSerializer

    def get(self, request):
        obj = Contact.objects.last()
        serializer =ContactSerializer(obj, context={'request': request})
        return Response(serializer.data if obj else None)


@method_decorator(csrf_exempt, name='dispatch')
@extend_schema(
    request=FeedbackSerializer,
    responses={
        200: {"message": "Feedback sent successfully"},
        400: {"error": "All fields are required"},
        500: {"error": "Internal server error"}
    }
)
class FeedbackView(GenericAPIView):
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            # Запускаем отправку письма в отдельном потоке
            Thread(target=send_feedback_email, kwargs=serializer.validated_data).start()

            # Возвращаем ответ сразу, не дожидаясь завершения отправки
            return Response(
                {"message": "Feedback sent successfully"},
                status=status.HTTP_200_OK
            )

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

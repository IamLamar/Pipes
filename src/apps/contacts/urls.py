from django.urls import path

from apps.contacts.views import ContactSingleView, FeedbackView


urlpatterns = [
    path("", ContactSingleView.as_view(), name="contact-single"),
    path('applications/', FeedbackView.as_view(), name='application-create'),
]

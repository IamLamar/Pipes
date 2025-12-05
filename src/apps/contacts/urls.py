from django.urls import path

from apps.contacts.views import AcceptancePersonView, ContactSingleView, FeedbackView


urlpatterns = [
    path("", ContactSingleView.as_view(), name="contact-single"),
    path('applications/', FeedbackView.as_view(), name='application-create'),
    path('acceptance-person/', AcceptancePersonView.as_view(), name='acceptance-person'),
]

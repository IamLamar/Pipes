from django.urls import path
from .views import (
    CompanyInNumbersListView,
    CompanyPhotoView,
    CompanyValueListView,
    DocumentsListView,
    ExpertsListView,
)

urlpatterns = [
    path('in-numbers/', CompanyInNumbersListView.as_view()),
    path('values/', CompanyValueListView.as_view()),
    path('experts/', ExpertsListView.as_view()),
    path('photo/', CompanyPhotoView.as_view()),
    path('documents/', DocumentsListView().as_view()),
]

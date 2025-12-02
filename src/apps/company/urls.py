from django.urls import path
from .views import (
    CompanyInNumbersListView,
    CompanyValueListView,
    ExpertsListView,
)

urlpatterns = [
    path('in-numbers/', CompanyInNumbersListView.as_view()),
    path('values/', CompanyValueListView.as_view()),
    path('experts/', ExpertsListView.as_view()),
]

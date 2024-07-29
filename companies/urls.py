from django.contrib import admin
from django.urls import path

from companies.apps import CompaniesConfig
from companies.views import CompaniesCreateView, CompaniesListView, CompaniesDetailView, CompaniesUpdateView, \
    CompaniesDeleteView

app_name = CompaniesConfig.name

urlpatterns = [
    path('create/', CompaniesCreateView.as_view(), name='create'),
    path('', CompaniesListView.as_view(), name='list'),
    path('view/<int:pk>/', CompaniesDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', CompaniesUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CompaniesDeleteView.as_view(), name='delete'),
]

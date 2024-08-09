from django.contrib import admin
from django.urls import path

from companies.apps import CompaniesConfig
from companies.views import CompaniesCreateView, CompaniesListView, CompaniesDetailView, CompaniesUpdateView, \
    CompaniesDeleteView

app_name = CompaniesConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', CompaniesCreateView.as_view(), name='create'),
    path('', CompaniesListView.as_view(), name='list'),
    path('view/<slug:the_slug_comp>/', CompaniesDetailView.as_view(), name='view'),
    path('edit/<slug:the_slug_comp>/', CompaniesUpdateView.as_view(), name='edit'),
    path('delete/<slug:the_slug_comp>/', CompaniesDeleteView.as_view(), name='delete'),
]

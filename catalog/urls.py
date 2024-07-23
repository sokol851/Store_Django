from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, feedback

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
]

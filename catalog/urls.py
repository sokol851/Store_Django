from django.contrib import admin
from django.urls import path

from catalog.views import index, contacts

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contacts/', contacts),
]

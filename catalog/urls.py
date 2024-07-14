from django.contrib import admin
from django.urls import path

from catalog.views import index, contacts, feedback

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contacts/', contacts),
    path('feedback/', feedback),
]

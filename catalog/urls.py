from django.contrib import admin
from django.urls import path

from catalog.views import catalog, contacts

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog),
    path('/contacts', contacts)
]

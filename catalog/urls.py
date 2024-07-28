from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, feedback, product_page, create_product

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('product_page/<int:pk>', product_page, name='product_page'),
    path('create_product/', create_product, name='create_product'),
]

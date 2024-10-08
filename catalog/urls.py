from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ContactsListView, FeedbackCreateView, FeedbackListView, ProductListView, ProductDetailView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contacts/', ContactsListView.as_view(), name='contacts'),

    path('create_feedback/', FeedbackCreateView.as_view(), name='create_feedback'),
    path('list_feedback/', FeedbackListView.as_view(), name='list_feedback'),
    path('', ProductListView.as_view(), name='index'),
    path('detail_prod/<slug:the_slug_prod>', cache_page(60)(ProductDetailView.as_view()), name='product_page'),
    path('update_prod/<slug:the_slug_prod>', ProductUpdateView.as_view(), name='update_product'),
    path('created_prod/', ProductCreateView.as_view(), name='create_product'),
    path('delete_prod/<slug:the_slug_prod>/', ProductDeleteView.as_view(), name='delete_product'),
    path('activity_prod/<int:pk>/', ProductUpdateView.toggle_activity, name='toggle_activity_prod'),
    path("category_list", CategoryListView.as_view(), name="category_list")
]

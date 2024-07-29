from django.contrib import admin
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsListView, FeedbackCreateView, FeedbackListView, ProductListView, ProductDetailView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, BlogCreateView, BlogUpdateView, BlogDeleteView, \
    BlogDetailView, BlogListView

app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),

    path('contacts/', ContactsListView.as_view(), name='contacts'),

    path('create_feedback/', FeedbackCreateView.as_view(), name='create_feedback'),
    path('list_feedback/', FeedbackListView.as_view(), name='list_feedback'),

    path('', ProductListView.as_view(), name='index'),
    path('detail_prod/<slug:the_slug_prod>', ProductDetailView.as_view(), name='product_page'),
    path('update_prod/<slug:the_slug_prod>', ProductUpdateView.as_view(), name='update_product'),
    path('created_prod/', ProductCreateView.as_view(), name='create_product'),
    path('delete_prod/<slug:the_slug_prod>/', ProductDeleteView.as_view(), name='delete_product'),
    path('activity_prod/<int:pk>/', ProductUpdateView.toggle_activity, name='toggle_activity_prod'),

    path('list_blog/', BlogListView.as_view(), name='list_blog'),
    path('created_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('update_blog/<slug:the_slug_blog>', BlogUpdateView.as_view(), name='update_blog'),
    path('delete_blog/<slug:the_slug_blog>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('detail_blog/<slug:the_slug_blog>', BlogDetailView.as_view(), name='detail_blog'),
    # path('activity_prod/<int:pk>/', BlogUpdateView.toggle_activity, name='toggle_activity_prod'),

]

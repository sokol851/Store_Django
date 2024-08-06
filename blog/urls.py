from django.contrib import admin
from django.urls import path

from blog.apps import BlogConfig

from blog.views import BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, BlogListView

app_name = BlogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogListView.as_view(), name='list_blog'),
    path('created_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('update_blog/<slug:the_slug_blog>', BlogUpdateView.as_view(), name='update_blog'),
    path('delete_blog/<slug:the_slug_blog>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('detail_blog/<slug:the_slug_blog>', BlogDetailView.as_view(), name='detail_blog'),
    path('activity_blog/<int:pk>/', BlogUpdateView.toggle_activity, name='toggle_activity_blog'),

]

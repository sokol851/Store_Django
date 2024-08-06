from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_published', 'views_count',)
    list_filter = ('name', 'created_at', 'is_published', 'views_count',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

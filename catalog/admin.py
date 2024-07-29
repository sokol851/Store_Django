from django.contrib import admin

from catalog.models import Product, Category, Contacts, Feedback, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_active', 'slug')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('warehouse_address', 'legal_address', 'working_hours', 'phone', 'email',)


@admin.register(Feedback)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'content',)
    list_filter = ('name', 'email',)
    search_fields = ('name', 'email',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_published', 'views_count',)
    list_filter = ('name', 'created_at', 'is_published', 'views_count',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

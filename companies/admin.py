from django.contrib import admin

from companies.models import Companies


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_published', )
    list_filter = ('title', 'is_published', )
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

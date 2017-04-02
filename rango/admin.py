from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

admin.site.register(Page,PageAdmin)

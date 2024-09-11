from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'text', 'price')
    list_display_links = ('pk', 'name')


admin.site.register(Product, ProductAdmin)

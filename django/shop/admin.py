from django.contrib import admin

from .models import *
from .models import Product

admin.site.register(Product)

@admin.register(Category)   
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category','is_active')
    list_filter = ('category','is_active')
    search_fields = ('name', 'description')

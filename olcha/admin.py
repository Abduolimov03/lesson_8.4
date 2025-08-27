from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ['title', 'slug']
    prepopulated_fields = {"slug":("title", )}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title", )}
# admin.site.register(Product)
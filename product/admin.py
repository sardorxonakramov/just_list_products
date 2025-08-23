from django.contrib import admin
from .models import *
# from .models.category import Category
# from .models.product import Product
# from .models.product_image import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "is_main")
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "is_active", "created_at")
    list_filter = ("category", "is_active", "created_at")
    search_fields = ("title", "feature", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductImageInline]

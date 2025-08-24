from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Category, Product, ProductImage


# CKEditor qo‘llash uchun custom forma
class ProductAdminForm(forms.ModelForm):
    feature = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = "__all__"


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
    form = ProductAdminForm  # CKEditor ishlashi uchun custom forma
    list_display = ("title", "category", "price", "is_active", "created_at")
    list_filter = ("category", "is_active", "created_at")
    search_fields = ("title", "feature", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductImageInline]

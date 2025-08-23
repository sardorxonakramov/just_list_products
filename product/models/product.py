from .category import Category
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")
    
    feature = models.TextField(verbose_name="Xususiyat")
    description = models.TextField(verbose_name="Ta'rif", blank=True, null=True)

    purchase_price = models.DecimalField(
        verbose_name="Sotib olingan narx", max_digits=10, decimal_places=2, blank=True, null=True
    )
    price = models.DecimalField(verbose_name="Sotish narxi", max_digits=10, decimal_places=2)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_final_price(self):
        # Hozircha faqat oddiy narx qaytaradi
        return self.price

    def __str__(self):
        return self.title

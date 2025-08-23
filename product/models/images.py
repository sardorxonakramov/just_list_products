from django.db import models
from django.utils.text import slugify


class ProductImage(models.Model):
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product/")
    is_main = models.BooleanField(default=False, verbose_name="Asosiy Rasim")

    class Meta:
        db_table = "product_images"
        verbose_name = "Product Image"
        verbose_name_plural ="Product Images"
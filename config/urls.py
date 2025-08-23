from django.contrib import admin
from django.urls import path
from product.views import product_list, product_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),  # Mahsulotlar ro'yxati
    path("<slug:slug>/", product_detail, name="product_detail"),
]


if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)
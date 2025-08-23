from django.shortcuts import render
from .models.product import Product
from .models.category import Category

def product_list(request):
    products = Product.objects.filter(is_active=True).prefetch_related("images")
    categories = Category.objects.filter(is_active=True)

    # filter parametrlari
    category_id = request.GET.get("category")
    sort = request.GET.get("sort")
    view_mode = request.GET.get("view", "grid")  # default grid bo‘ladi

    if category_id:
        products = products.filter(category_id=category_id)

    if sort == "asc":
        products = products.order_by("price")
    elif sort == "desc":
        products = products.order_by("-price")

    context = {
        "products": products,
        "categories": categories,
        "view_mode": view_mode,
    }
    return render(request, "product_list.html", context)


from django.shortcuts import render, get_object_or_404
from product.models import Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "detail.html", {"product": product})

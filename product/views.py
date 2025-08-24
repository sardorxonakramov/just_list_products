from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.prefetch_related("images").all()
    categories = Category.objects.all()

    # filterlar
    category_id = request.GET.get("category")
    sort = request.GET.get("sort")
    view = request.GET.get("view", "grid")  # default grid

    if category_id:
        products = products.filter(category_id=category_id)

    if sort == "asc":
        products = products.order_by("price")
    elif sort == "desc":
        products = products.order_by("-price")

    # pagination
    paginator = Paginator(products, 40)  # sahifada 2 ta mahsulot
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # query_params
    query_params = request.GET.copy()
    if "page" in query_params:
        query_params.pop("page")

    context = {
        "products": page_obj,
        "categories": categories,
        "page_obj": page_obj,
        "query_params": query_params,
        "view": view,
    }
    return render(request, "product_list.html", context)



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # Narxni formatlash (vergul o‘rniga bo‘sh joy qo‘yamiz)
    formatted_price = f"{product.price:,.0f}".replace(",", " ")
    return render(request, "detail.html", {
        "product": product,
        "formatted_price": formatted_price
    })

"""Aplication logic"""

from django.shortcuts import get_object_or_404, render

from shopcart.forms import CartAddProductForm

from .models import Product


def index(request):
    return render(request, "main/main.html")


def check_product(request):
    return render(request, "main/product.html")


def shop(request):
    product = Product.objects.all()
    context = {"pr": product}
    return render(request, "main/product.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "main/product_details.html",
        {"product": product, "cart_product_form": cart_product_form},
    )

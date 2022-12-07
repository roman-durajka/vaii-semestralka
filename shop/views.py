from django.shortcuts import render
from shop.models import Product

# Create your views here.


def cart(request):
    cart_items = Product.objects.all()
    return render(request, "cart.html", {"cart_items": cart_items})


def cart_price(request):
    cart_items = Product.objects.all()
    price = 0
    for item in cart_items:
        price += item.price

    return price

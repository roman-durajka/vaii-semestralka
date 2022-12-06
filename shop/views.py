from django.shortcuts import render
from shop.models import Product

# Create your views here.


def cart(request):
    cart_items = Product.objects.all()
    return render(request, "cart.html", {"cart_items": cart_items})

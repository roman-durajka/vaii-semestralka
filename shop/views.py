from django.shortcuts import render, redirect
from shop.models import Product
from django.http import HttpResponse


# Create your views here.


def cart(request):
    return render(request, "cart.html", {"cart_items": request.session["cart"]})


def cart_add(request, product_id):
    try:
        request.session["cart"][str(product_id)]["quantity"] += 1
    except:
        product = Product.objects.get(pk=product_id)
        product_dict = {"quantity": 1, "preview": product.preview, "name": product.name, "text": product.text, "price": product.price}
        request.session["cart"][str(product_id)] = product_dict
    request.session.modified = True

    return redirect("shop:cart")


def cart_remove(request, product_id):
    del request.session["cart"][str(product_id)]
    request.session.modified = True

    return redirect("shop:cart")


def cart_price(request):
    price = 0

    for product_id, value in request.session["cart"].items():
        price += value["price"]

    return HttpResponse(str(price))

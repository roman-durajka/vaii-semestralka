from django.shortcuts import render, redirect
from shop.models import Product
from django.http import HttpResponse, JsonResponse


# Create your views here.


def cart(request):
    try:
        if request.session["cart"]:
            pass
    except:
        request.session["cart"] = {}
    return render(request, "cart.html", {"cart_items": request.session["cart"]})


def cart_add(request):
    element_id = request.POST.get("id")
    product_id = "".join([s for s in element_id if s.isdigit()])

    try:
        quantity = int(request.session["cart"][product_id]["quantity"])
        request.session["cart"][product_id]["quantity"] = quantity + 1
    except:
        product = Product.objects.get(pk=int(product_id))
        product_dict = {"quantity": 1, "preview": product.preview, "name": product.name, "text": product.text, "price": product.price}
        request.session["cart"][product_id] = product_dict
    request.session.modified = True

    return HttpResponse(status=200)


def cart_remove(request):
    element_id = request.POST.get("id")
    str_id = "".join([s for s in element_id if s.isdigit()])
    del request.session["cart"][str_id]
    request.session.modified = True

    return HttpResponse(status=200)


def cart_info(request):
    price = 0
    info = {}

    for product_id, value in request.session["cart"].items():
        price += value["price"] * int(value["quantity"])
        info[product_id] = value
    info["price"] = price

    return JsonResponse(info)


def update_quantity(request):
    element_id = request.POST.get("id")
    value = request.POST.get("value")
    str_id = "".join([s for s in element_id if s.isdigit()])
    request.session["cart"][str_id]["quantity"] = value
    request.session.modified = True

    return HttpResponse(status=200)

from django.shortcuts import render
from shop.models import Product, Order
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from django.contrib.auth.decorators import login_required


# Create your views here.


OBJECTS_ON_PAGE = 2


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
        if product_id == "price":
            continue
        price += value["price"] * int(value["quantity"])
        info[product_id] = value
    info["price"] = price
    request.session["cart"]["price"] = price
    request.session.modified = True

    return JsonResponse(info)


def update_quantity(request):
    element_id = request.POST.get("id")
    value = request.POST.get("value")
    str_id = "".join([s for s in element_id if s.isdigit()])
    request.session["cart"][str_id]["quantity"] = int(value)
    request.session.modified = True

    return HttpResponse(status=200)


def submit_cart(request):
    email_address = request.POST.get("email")
    price = request.session["cart"]["price"]
    del request.session["cart"]["price"]
    json_field = request.session["cart"]

    order = Order(email=email_address, price=price, data=json_field)
    order.save()
    request.session["cart"] = {}

    return HttpResponse(200)


def stock(request):
    message = ""
    if len(request.session["cart"]) <= 1:
        message += "Your cart is empty!"
    for product_id, data in request.session["cart"].items():
        if product_id == "price":
            continue
        db_item = Product.objects.get(id=product_id)
        if db_item.stock < int(data["quantity"]):
            message += f"Item {data['name']} does not have enough stock! There are {db_item.stock} available pieces.\n"

    if not message:
        for product_id, data in request.session["cart"].items():
            if product_id == "price":
                continue
            db_item = Product.objects.get(id=product_id)
            db_item.stock -= int(data["quantity"])
            Product.save(db_item)

    return JsonResponse({"message": message})


def paginate(request):
    page = int(request.POST.get("page"))

    starting_number = (page - 1) * OBJECTS_ON_PAGE
    ending_number = page * OBJECTS_ON_PAGE

    result = Order.objects.filter()[starting_number:ending_number]

    data = serializers.serialize('json', result)

    return JsonResponse(data, safe=False)


@login_required(login_url="/accounts/login")
def orders(request):
    shop_objs = Order.objects.filter()

    paginator = Paginator(shop_objs, OBJECTS_ON_PAGE)
    page = request.GET.get('page', 1)

    try:
        results_objs = paginator.page(page)
    except PageNotAnInteger:
        results_objs = paginator.page(1)
    except EmptyPage:
        results_objs = paginator.page(paginator.num_pages)

    page_list = results_objs.paginator.page_range

    return render(request, "orders.html", {"page_list": page_list})

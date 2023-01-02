from django.shortcuts import render, redirect
from playground.models import News
from gallery.models import GalleryItem
from shop.models import Product
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def home(request):
    news = News.objects.all()
    return render(request, "index.html", {"news": news})


def gallery(request):
    gallery_items = GalleryItem.objects.all()
    return render(request, "gallery.html", {"gallery": gallery_items})


def faq(request):
    return render(request, "faq.html")


def contribute(request):
    try:
        if request.session["cart"]:
            pass
    except:
        request.session["cart"] = {}
    products = Product.objects.all()
    return render(request, "contribute.html", {"products": products})


@login_required(login_url="/accounts/login")
def create_news(request):
    if request.method == "POST":
        form = forms.CreateNews(request.POST)
        if form.is_valid():
            uncommitted_form = form.save(commit=False)
            uncommitted_form.author = request.user
            uncommitted_form.save()
        return redirect("home")
    else:
        form = forms.CreateNews()
    return render(request, "create_news.html", {"form": form})


@login_required(login_url="/accounts/login")
def delete_news(_, news_id):
    instance = News.objects.get(id=news_id)
    instance.delete()

    return redirect("home")


@login_required(login_url="/accounts/login")
def edit_news(request, news_id=None):
    if request.method == "POST":
        form = forms.EditNews(request.POST)
        if form.is_valid():
            news = News.objects.filter(id=news_id)
            fields = form.cleaned_data
            news.update(**fields)
        return redirect("home")
    else:
        news = News.objects.get(id=news_id)
        form = forms.EditNews(instance=news)
    return render(request, "edit_news.html", {"form": form, "id": news_id})

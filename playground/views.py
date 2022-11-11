from django.shortcuts import render
from playground.models import News

# Create your views here.


def home(request):
    news = News.objects.all()
    return render(request, "index.html", {"news": news})


def gallery(request):
    return render(request, "gallery.html")


def faq(request):
    return render(request, "faq.html")


def contribute(request):
    return render(request, "contribute.html")

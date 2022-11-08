from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")

def faq(request):
    return render(request, "faq.html")

def contribute(request):
    return render(request, "contribute.html")

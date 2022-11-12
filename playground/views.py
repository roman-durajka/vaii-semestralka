from django.shortcuts import render, redirect
from playground.models import News
from django.contrib.auth.decorators import login_required
from . import forms

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

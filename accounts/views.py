from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # todo: login
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # todo: login
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

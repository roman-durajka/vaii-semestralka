from django.shortcuts import redirect
from . import forms

# Create your views here.


def submit_idea(request):
    if request.method == "POST":
        form = forms.GalleryIdea(request.POST)
        if form.is_valid():
            form.save()
    return redirect("gallery")

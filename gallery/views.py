from django.shortcuts import render, redirect
from .models import GalleryItem
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
@login_required(login_url="/accounts/login")
def create_gallery_item(request):
    if request.method == "POST":
        form = forms.GalleryItem(request.POST)
        if form.is_valid():
            uncommitted_form = form.save(commit=False)
            uncommitted_form.author = request.user
            uncommitted_form.save()
    return redirect("gallery")


@login_required(login_url="/accounts/login")
def delete_gallery_item(_, gallery_item_id):
    instance = GalleryItem.objects.get(id=gallery_item_id)
    instance.delete()

    return redirect("gallery")


@login_required(login_url="/accounts/login")
def edit_gallery_item(request, gallery_item_id):
    if request.method == "POST":
        form = forms.GalleryItem(request.POST)
        if form.is_valid():
            gallery_item = GalleryItem.objects.filter(id=gallery_item_id)
            fields = form.cleaned_data
            gallery_item.update(**fields)
    return redirect("gallery")


@login_required(login_url="/accounts/login")
def edit_gallery(request):
    gallery_items = GalleryItem.objects.all()

    created_forms = []
    for gallery_item in gallery_items:
        form = forms.GalleryItem(instance=gallery_item)
        created_forms.append({"form": form, "id": gallery_item.id})

    new_form = forms.GalleryItem()
    created_forms.append({"form": new_form, "id": None})

    return render(request, "edit_gallery.html", {"data": created_forms})

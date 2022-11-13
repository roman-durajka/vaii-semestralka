from django import forms
from . import models


class GalleryItem(forms.ModelForm):
    class Meta:
        model = models.GalleryItem
        fields = ["name", "text", "source", "preview"]

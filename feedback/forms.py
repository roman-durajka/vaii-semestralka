from django import forms
from . import models


class GalleryIdea(forms.ModelForm):
    class Meta:
        model = models.GalleryIdea
        fields = ["email", "text"]

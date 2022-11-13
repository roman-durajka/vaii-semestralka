from django import forms
from . import models


class CreateNews(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ["title", "text", "source", "preview", "media"]


class EditNews(forms.ModelForm):
    class Meta:
        model = models.News
        fields = ["title", "text", "source", "preview", "media"]

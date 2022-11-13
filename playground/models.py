from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    source = models.URLField()
    preview = models.URLField()
    media = models.URLField(max_length=256, default=None, blank=True)
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

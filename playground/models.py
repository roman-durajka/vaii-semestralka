from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    source = models.CharField(max_length=256)
    preview = models.CharField(max_length=256)
    media = models.CharField(max_length=256, default=None, blank=True)

    def __str__(self):
        return self.title

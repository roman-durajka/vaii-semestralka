from django.db import models


# Create your models here.
class GalleryItem(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    source = models.URLField()
    preview = models.URLField()

    def __str__(self):
        return self.name

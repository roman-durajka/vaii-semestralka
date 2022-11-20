from django.db import models

# Create your models here.


class GalleryIdea(models.Model):
    email = models.EmailField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.email

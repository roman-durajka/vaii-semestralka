from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    # add in thumbnail later

    def __str__(self):
        return self.title

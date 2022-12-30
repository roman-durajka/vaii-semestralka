from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256)
    text = models.TextField()
    price = models.IntegerField()
    preview = models.URLField()
    stock = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    email = models.EmailField()
    price = models.IntegerField()
    data = models.JSONField()

    def __str__(self):
        return self.email


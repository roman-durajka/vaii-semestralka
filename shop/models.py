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


class Cart(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.item


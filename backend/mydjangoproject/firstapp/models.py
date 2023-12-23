from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)

from django.db import models
from products.models import Product
# Create your models here.

class Review(models.Model):
    prod_num = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
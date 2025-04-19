# Create your models here.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

# catalog/models.py

from django.db import models

class Product(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    preu = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
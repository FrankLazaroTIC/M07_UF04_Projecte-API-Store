# orders/models.py

from django.db import models

class Order(models.Model):
    cart = models.OneToOneField('carreto.Cart', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
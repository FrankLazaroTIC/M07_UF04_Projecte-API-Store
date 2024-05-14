# orders/models.py

from django.db import models
from cart.models import Cart

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
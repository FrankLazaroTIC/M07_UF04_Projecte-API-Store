from django.db import models

class Cart(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('cataleg.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
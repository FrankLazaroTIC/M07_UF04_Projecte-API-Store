# payments/models.py

from django.db import models

class Payment(models.Model):
    order = models.OneToOneField('comandes.Order', on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    cvc = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
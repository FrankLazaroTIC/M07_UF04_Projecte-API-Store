from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognoms = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom + " " + self.cognoms
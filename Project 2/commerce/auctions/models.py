from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=64,unique=True)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.username}"

class auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    bid = models.DecimalField(max_digits=19,decimal_places=2)
    category = models.CharField(max_length=12)
    image = models.CharField(max_length=64,blank=True)
    time = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=64)
    current_bid = models.DecimalField(max_digits=19,decimal_places=2)
    
    def __str__(self):
        return f"{self.title}"

class bids(models.Model):
    username = models.CharField(max_length=64)
    current_bid = models.DecimalField(max_digits=19,decimal_places=2)
    item_name = models.CharField(max_length=64)

class comments(models.Model):
    pass



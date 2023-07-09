from django.db import models
from django.contrib.auth.models import User


class ContactEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    product_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    meat_or_fish = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.product_name

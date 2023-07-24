from django.db import models


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    objects = models.Manager()

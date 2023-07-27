from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)


class Trip(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    max_people = models.PositiveIntegerField()

    class Meta:
        ordering = ['date_from']


class Client(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    pesel = models.CharField(max_length=255)


class ClientTrip(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='trips')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='clients')
    registered_at = models.DateTimeField(auto_now_add=True)
    payment_date = models.DateTimeField(null=True)


class CountryTrip(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='trips')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='countries')
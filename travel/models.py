from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

class TravelPackage(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    available = models.BooleanField(default=True)

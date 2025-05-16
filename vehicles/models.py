from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
#class FuelType(models.Model):
#    name = models.CharField(max_length=50)
#    desc = models.TextField()
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#
#    def __str__(self):
#        return self.name

class Vehicle(models.Model):
    HYBRID = "HY"
    GASOLINE = "GS"
    DIESEL = "DS"
    ELECTRIC = "EC"
    FUEL_TYPE_CHOICES = {
        HYBRID: "Hybrid",
        ELECTRIC: "Electric",
        DIESEL: "Diesel",
        GASOLINE: "Gasoline",
    }

    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    fuel_type = models.CharField(
        max_length=2, 
        choices=FUEL_TYPE_CHOICES, 
        default=HYBRID,
    )
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    vin = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

from django.db import models

class Apartment(models.Model):
    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    apartment_img = models.ImageField(null=True, blank=True, upload_to="images/")
    monthly_rent = models.DecimalField(max_digits=7, decimal_places=2)
    renovated = models.BooleanField()
    air_conditioning = models.BooleanField()
    pool = models.BooleanField()
    allows_pets = models.BooleanField()
    laundry_onsite = models.BooleanField()

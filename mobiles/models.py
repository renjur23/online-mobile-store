from django.db import models
from django.urls import reverse


class Mobile(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, default=False)
    mobile_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name

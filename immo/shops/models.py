from django.contrib.gis.db import models


class Shop(models.Model):
    price = models.CharField(max_length=100)
    location = models.PointField()
    surface = models.CharField(max_length=100)


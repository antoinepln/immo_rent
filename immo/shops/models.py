from django.contrib.gis.db import models

class User_loc(models.Model):
    location = models.PointField()



class Shop(models.Model):
    price = models.CharField(max_length=100)
    location = models.PointField()
    surface = models.CharField(max_length=100)


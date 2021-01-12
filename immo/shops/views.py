from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = 2.3712272
latitude = 48.8544433

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:100]
    template_name = "shops/index.html"


home = Home.as_view()


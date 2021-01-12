from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr
from .models import Shop

from django.views.generic import TemplateView
from .forms import HomeForm
from django.shortcuts import render

import requests, json
import urllib.parse

api_url = "https://api-adresse.data.gouv.fr/search/?q="

longitude = 2.3712272
latitude = 48.8544433

user_location = Point(longitude, latitude, srid=4326)

#class HomeView(generic.ListView):
    #model = Shop
    #context_object_name = "shops"
    #queryset = Shop.objects.annotate(distance=Distance("location", user_location)
    #).order_by("distance")[0:100]
    #template_name = "shops/index.html"

class Home(TemplateView):
    template_name = "shops/index.html"

    def get(self, request):
        form = HomeForm()

        shop = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:100]


        return render(request, self.template_name, {'form':form,'shops': shop})

    def post(self, request):


        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['location']

        adr = text
        r = requests.get(api_url + urllib.parse.quote(adr))
        d = json.loads(r.content.decode('unicode_escape'))
        loc = d['features'][0]['geometry']['coordinates']

        user_location = fromstr(f'POINT({loc[0]} {loc[1]})', srid=4326)
        shop = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:100]

        args = {'form':form, 'text':user_location, 'shops':shop}
        return render(request, self.template_name,args)



#class Home(HomeView, TemplateView):



#home =  HomeView.as_view()


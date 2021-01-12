from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop, User_loc

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('price','surface','location')

@admin.register(User_loc)
class User_loc(OSMGeoAdmin):
    list_display = ['location']






# Register your models here.

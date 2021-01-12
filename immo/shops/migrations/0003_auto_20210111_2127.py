
from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'data.json'


def load_data(apps, schema_editor):
    Shop = apps.get_model('shops', 'Shop')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects:
            try:
                prix = obj['price']
                surface = obj.get('surface')
                longitude = obj.get('coordinates')[0]
                latitude = obj.get('coordinates')[1]
                location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                Shop(price=prix, location = location, surface = surface).save()
            except KeyError:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]

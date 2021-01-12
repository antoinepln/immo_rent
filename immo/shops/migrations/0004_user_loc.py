# Generated by Django 3.1.5 on 2021-01-12 11:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20210111_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_loc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]

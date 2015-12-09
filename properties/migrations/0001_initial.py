# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Price', models.IntegerField(max_length=50)),
                ('ContractType', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('LocationName', models.CharField(max_length=50)),
                ('Latitude', models.FloatField(max_length=50)),
                ('Longitude', models.FloatField(max_length=50)),
                ('Area', models.CharField(max_length=50)),
                ('FeaturesDesc', models.TextField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-03 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import medweb.homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0025_evaluation_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='home_phone',
            field=models.CharField(blank=True, max_length=12, validators=[medweb.homepage.models.phone_validator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='office_phone',
            field=models.CharField(max_length=12, validators=[medweb.homepage.models.phone_validator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='office_phone_extension',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]

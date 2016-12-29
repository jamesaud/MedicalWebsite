# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-08 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import medweb.homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_evaluation_net_income_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='office_phone_extension',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='person',
            name='home_phone',
            field=models.CharField(blank=True, default=-2855, max_length=15, validators=[medweb.homepage.models.phone_validator]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='office_phone',
            field=models.CharField(blank=True, default='', max_length=15, validators=[medweb.homepage.models.phone_validator]),
            preserve_default=False,
        ),
    ]
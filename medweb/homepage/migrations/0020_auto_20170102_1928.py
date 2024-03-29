# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-03 00:28
from __future__ import unicode_literals

from django.db import migrations, models
import medweb.homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_randomreferral_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='ehr_support_vendors',
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='group_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='office_phone',
            field=models.CharField(max_length=15, validators=[medweb.homepage.models.phone_validator]),
        ),
    ]

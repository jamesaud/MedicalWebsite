# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-22 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import medweb.homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=8882223333, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='group_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='home_phone',
            field=models.CharField(default=2223334444, max_length=15, validators=[medweb.homepage.models.phone_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='message',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='person',
            name='office_phone',
            field=models.CharField(default=2223334444, max_length=15, validators=[medweb.homepage.models.phone_validator]),
            preserve_default=False,
        ),
    ]
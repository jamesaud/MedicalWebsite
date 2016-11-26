# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-25 19:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20161125_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 25, 19, 57, 47, 626999, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 11, 25, 19, 57, 52, 165795, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-03 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_auto_20170102_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='revenue_labs',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-07 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20161126_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='current_system',
        ),
    ]
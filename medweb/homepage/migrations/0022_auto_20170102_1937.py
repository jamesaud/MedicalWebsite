# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-03 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_auto_20170102_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='hr_staff',
            new_name='hr_total_staff',
        ),
    ]
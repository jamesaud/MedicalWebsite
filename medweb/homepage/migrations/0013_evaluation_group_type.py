# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-07 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_evaluation_current_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='group_type',
            field=models.CharField(choices=[('MS', 'MS'), ('Solo', 'Solo'), ('Other', 'Other')], default='Solo', max_length=255),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-29 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20161207_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomReferral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral', models.CharField(blank=True, choices=[('LinkedIn', 'LinkedIn'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Google', 'Google'), ('Other', 'Other')], max_length=255)),
            ],
        ),
    ]

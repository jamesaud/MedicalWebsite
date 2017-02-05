# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-28 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0029_auto_20170103_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='current_system',
            field=models.CharField(blank=True, choices=[('Abraxas', 'Abraxas'), ('AdvancedMD', 'AdvancedMD'), ('Allscripts', 'Allscripts'), ('Aprima', 'Aprima'), ('Athena', 'Athena'), ('Cerner', 'Cerner'), ('CompuGroup', 'CompuGroup'), ('CureMD', 'CureMD'), ('E-MDs', 'E-MDs'), ('Epic', 'Epic'), ('GE Healthcare', 'GE Healthcare'), ('Greenway', 'Greenway'), ('Kareo', 'Kareo'), ('McKesson', 'McKesson'), ('NextGen', 'NextGen'), ('Nextech', 'Nextech'), ('Optum', 'Optum'), ('Other', 'Other'), ('Platinum Systems', 'Platinum Systems'), ('Practice Fusion', 'Practice Fusion'), ('Vitera', 'Vitera'), ('eClinicalWorks', 'eClinicalWorks')], max_length=255),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='group_type',
            field=models.CharField(blank=True, choices=[('Single Specialty', 'Single Specialty'), ('Multi Specialty', 'Multi Specialty'), ('Hospital Based Clinic', 'Hospital Based Clinic'), ('Urgent Care', 'Urgent Care'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='total_revenue',
            field=models.CharField(blank=True, choices=[('1 - $499,999', '1 - 499,999'), ('500,000 - 999,999', '500,000 - 999,999'), ('1,000,000 - 4,999,999', '1,000,000 - 4,999,999'), ('5,000,000 - 9,999,999', '5,000,000 - 9,999,999'), ('10,000,000 - 24,999,999', '10,000,000 - 24,999,999'), ('25,000,000 - 49,999,999', '25,000,000 - 49,999,999'), ('50,000,000+', '50,000,000+')], max_length=255, null=True),
        ),
    ]

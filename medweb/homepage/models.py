# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models


class Person(models.Model):

    # First Name and Last Name do not cover name patterns around the globe.
    first_name = models.CharField(blank=False, null=False, max_length=255)
    last_name = models.CharField(blank=False, null=False, max_length=255)

    def __str__(self):
        return self.first_name + self.last_name


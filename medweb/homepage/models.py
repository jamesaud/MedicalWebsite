# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Phone_Regex is from:
# http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
# Writing custom validators:
# https://docs.djangoproject.com/en/1.10/ref/validators/
def phone_validator(value):
    return RegexValidator(regex=r'^\+?1?\d{9,15}$',
                          message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Person(models.Model):

    # First Name and Last Name do not cover name patterns around the globe.
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False)
    position = models.CharField(max_length=255)
    home_phone = models.CharField(validators=[phone_validator], max_length=15, blank=True, null=True)  # validators should be a list
    office_phone = models.CharField(validators=[phone_validator], max_length=15, blank=True, null=True)

    contacted = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Evaluation(models.Model):
    # Make Person the Primary Key for an evaluation. I.E. We can't have an evaluation without a person
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    group_name = models.CharField(max_length=255, blank=True)
    message = models.CharField(max_length=2000, blank=True)
    call_time = models.DateTimeField(null=True, blank=True)
    current_system = models.CharField(max_length=255, blank=True)

    ehr_support_vendors = models.IntegerField(null=True, blank=True)
    ehr_support_personnel = models.IntegerField(null=True, blank=True)
    ehr_likes = models.CharField(max_length=2000, blank=True)
    ehr_dislikes = models.CharField(max_length=2000, blank=True)

    hr_providers = models.IntegerField(null=True, blank=True)
    hr_it_staff = models.IntegerField(null=True, blank=True)
    hr_other_staff = models.IntegerField(null=True, blank=True)

    ehr_admin = models.IntegerField(null=True, blank=True)
    ehr_providers = models.IntegerField(null=True, blank=True)
    ehr_mas = models.IntegerField(null=True, blank=True)
    ehr_receptionists = models.IntegerField(null=True, blank=True)

    rcm_billers = models.IntegerField(null=True, blank=True)
    rcm_coders = models.IntegerField(null=True, blank=True)
    rcm_scribes = models.IntegerField(null=True, blank=True)
    rcm_collectors = models.IntegerField(null=True, blank=True)

    clearinghouse = models.CharField(max_length=512, blank=True)
    billing_company = models.CharField(max_length=512, blank=True)
    days_to_collect = models.IntegerField(null=True, blank=True)
    percent_ars = models.FloatField(null=True, blank=True)

    available_rooms = models.IntegerField(null=True, blank=True)
    revenue_labs = models.IntegerField(null=True, blank=True)
    doctors_recruit = models.CharField(max_length=2000, blank=True)
    total_revenue = models.FloatField(null=True, blank=True)

    referral = models.CharField(max_length=255, blank=True)
    monthly_newsletter =  models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return 'Evaluation of: ' + str(self.person)

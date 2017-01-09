# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


SYSTEM_CHOICES = (
    ('Abraxas', 'Abraxas'),
    ('AdvancedMD', 'AdvancedMD'),
    ('Allscripts', 'Allscripts'),
    ('Aprima', 'Aprima'),
    ('Athena', 'Athena'),
    ('Cerner', 'Cerner'),
    ('CompuGroup', 'CompuGroup'),
    ('CureMD', 'CureMD'),
    ('E-MDs', 'E-MDs'),
    ('Epic', 'Epic'),
    ('GE Healthcare', 'GE Healthcare'),
    ('Greenway', 'Greenway'),
    ('Kareo', 'Kareo'),
    ('McKesson', 'McKesson'),
    ('NextGen', 'NextGen'),
    ('Nextech', 'Nextech'),
    ('Optum', 'Optum'),
    ('Other', 'Other'),
    ('Platinum Systems', 'Platinum Systems'),
    ('Practice Fusion', 'Practice Fusion'),
    ('Vitera', 'Vitera'),
    ('eClinicalWorks', 'eClinicalWorks')
)

GROUP_TYPE_CHOICES = (
    ("Single Specialty", "Single Specialty"),
    ("Multi Specialty", "Multi Specialty"),
    ("Hospital Based Clinic", "Hospital Based Clinic"),
    ("Urgent Care", "Urgent Care"),
    ("Other", "Other"),
)

NET_INCOME_STATUS_CHOICES = (
    ("Decreased", "Decreased"),
    ("Same", "Stayed the Same"),
    ("Increased", "Increased"),
)

REFERRAL_CHOICES = (
    ('LinkedIn', "LinkedIn"),
    ('Facebook', "Facebook"),
    ('Twitter', "Twitter"),
    ('Google', "Google"),
    ('Referral', "Referral"),
    ('Industry Publication', "Industry Publication"),
    ('Other', "Other"),
)

REVENUE_CHOICES = (
    ('1 - $499,999', '1 - 499,999'),
    ('500,000 - 999,999', '500,000 - 999,999'),
    ('1,000,000 - 4,999,999', '1,000,000 - 4,999,999'),
    ('5,000,000 - 9,999,999', '5,000,000 - 9,999,999'),
    ('10,000,000 - 24,999,999', '10,000,000 - 24,999,999'),
    ('25,000,000 - 49,999,999', '25,000,000 - 49,999,999'),
    ('50,000,000+', '50,000,000+'),
)


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
    home_phone = models.CharField(validators=[phone_validator], max_length=12, blank=True)
    office_phone = models.CharField(validators=[phone_validator], max_length=12)
    office_phone_extension = models.CharField(max_length=12, blank=True)
    contacted = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.first_name + " " + self.last_name


# Every field here should be null (or blank if char field)
class Evaluation(models.Model):
    # Make Person the Primary Key for an evaluation. I.E. We can't have an evaluation without a person
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    demo = models.BooleanField(default=False) # Whether they signed up for a demo, or just an evaluation.

    group_name = models.CharField(max_length=255, blank=True)
    message = models.CharField(max_length=2000, blank=True)
    call_time = models.DateTimeField(null=True, blank=True)

    group_type = models.CharField(max_length=255, choices=GROUP_TYPE_CHOICES, blank=True)

    current_system = models.CharField(max_length=255, choices=SYSTEM_CHOICES, blank=True)

    ehr_support_personnel = models.IntegerField(null=True, blank=True)
    ehr_likes = models.CharField(max_length=2000, blank=True)
    ehr_dislikes = models.CharField(max_length=2000, blank=True)

    hr_total_staff = models.IntegerField(null=True, blank=True)
    hr_it_staff = models.IntegerField(null=True, blank=True)
    hr_other_staff = models.IntegerField(null=True, blank=True)

    ehr_admin = models.IntegerField(null=True, blank=True)
    ehr_providers = models.IntegerField(null=True, blank=True)
    ehr_mas = models.IntegerField(null=True, blank=True)
    ehr_receptionists = models.IntegerField(null=True, blank=True)
    ehr_scribes = models.IntegerField(null=True, blank=True)

    rcm_billers = models.IntegerField(null=True, blank=True)
    rcm_coders = models.IntegerField(null=True, blank=True)
    rcm_collectors = models.IntegerField(null=True, blank=True)

    clearinghouse = models.CharField(max_length=512, blank=True)
    billing_company = models.CharField(max_length=512, blank=True)
    days_to_collect = models.IntegerField(null=True, blank=True)
    percent_ars = models.FloatField(null=True, blank=True)

    available_rooms = models.IntegerField(null=True, blank=True)
    doctors_recruit = models.CharField(max_length=2000, blank=True)
    total_revenue = models.CharField(max_length=255, choices=REVENUE_CHOICES, null=True, blank=True)

    net_income_status = models.CharField(max_length=255, choices=NET_INCOME_STATUS_CHOICES, blank=True)

    referral = models.CharField(max_length=255, blank=True)
    monthly_newsletter = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True,)
    modified = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return 'Evaluation of: ' + str(self.person)

class RandomReferral(models.Model):
    referral = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.referral

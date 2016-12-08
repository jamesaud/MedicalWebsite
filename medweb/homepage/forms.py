# -*- coding: utf-8 -*-
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from medweb.homepage.models import Person, Evaluation
from parsley.decorators import parsleyfy
from forms import NoColonForm, AutoPlaceholderForm, EmptyChoiceField, EmptyTextarea
from config.settings.common import DATA_PARLSEY_PREFIX
from medweb.homepage.models import SYSTEM_CHOICES, GROUP_TYPE_CHOICES, NET_INCOME_STATUS_CHOICES, REFERRAL_CHOICES
from django.utils.translation import ugettext_lazy as _



@parsleyfy
class PersonForm(NoColonForm, AutoPlaceholderForm, ModelForm):
    class Meta:
        model = Person

        labels = {
            'office_phone_extension': _('Extension'),
        }


        fields = ('first_name', 'last_name', 'email', 'position', 'home_phone', 'office_phone', 'office_phone_extension')

        widgets = {'position': forms.TextInput(attrs={'placeholder': 'Title or Position'}),
                   'office_phone': forms.TextInput(attrs={'class': 'phone-autodash'}),
                   'office_phone_extension': forms.TextInput(attrs={'placeholder': 'ext'}),
                   }

        parsley_namespace = 'data-parsley'

"""
Make sure that no fields are required in the model itself, otherwise the dynamic ajax saving fails to work
"""
@parsleyfy
class EvaluationForm(NoColonForm, AutoPlaceholderForm,  ModelForm):

    # "11/25/2016 3:59 PM" is what we will receive
    call_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], required=False,)

    current_system = EmptyChoiceField(
        choices=SYSTEM_CHOICES,
        required=False,
        empty_label = 'Current System',)

    group_type = EmptyChoiceField(
        choices=GROUP_TYPE_CHOICES,
        required=False,
        empty_label = 'Group Type',)

    net_income_status = EmptyChoiceField(
        choices=NET_INCOME_STATUS_CHOICES,
        required=False,)

    referral = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=REFERRAL_CHOICES,)

    monthly_newsletter = forms.BooleanField(required=False)

    class Meta:
        model = Evaluation
        exclude = ('person',) # We inject person via ajax
        parsley_namespace = DATA_PARLSEY_PREFIX

        # Also will set placeholders because of AutoPlaceholderForm
        labels = {
            'ehr_support_vendors': _('# EHR support vendors'),
            'ehr_support_personnel': _('# EHR support personnel'),
            'hr_providers': _('# Providers'),
            'hr_it_staff': _('# IT staff'),
            'hr_other_staff': _('# Other staff'),
            'ehr_admin': _('# Admin'),
            'ehr_providers': _('# Providers'),
            'ehr_mas': _('# MAs'),
            'ehr_receptionists': _('# Receptionists'),
            'rcm_billers': _('# Billers'),
            'rcm_coders': _('# Coders'),
            'rcm_scribes': _('# Scribes'),
            'rcm_collectors': _('# Collectors'),
            'doctors_recruit': _('Are you trying to recruit doctors? How many and which specialities?'),
            #'monthly_newsletter': _('Yes'), # Couldn't get this to work

        }

        widgets = {'message': EmptyTextarea(attrs={'placeholder':'What would you like to say?'}),
                   'ehr_likes': EmptyTextarea(attrs={'placeholder':'What I like about my current EHR'}),
                   'ehr_dislikes': EmptyTextarea(attrs={'placeholder':'What I dislike about my current EHR'}),
                   'days_to_collect': forms.TextInput(attrs={'placeholder': '5'}),
                   'percent_ars': forms.TextInput(attrs={'placeholder': '20'}),
                   'doctors_recruit': EmptyTextarea(attrs={'placeholder': 'Yes, 2-3 more pediatric doctors and 1 more orthopedic surgeon.'}),
                   }


    # Have to update call time attrs in init, can't use widgets (not sure why)
    def __init__(self, *args, **kwargs):
        super(EvaluationForm, self).__init__(*args, **kwargs)
        self.fields['call_time'].widget.attrs \
            .update({
            'placeholder': 'Best time to call',
            'class': 'datetimepicker3',
        })


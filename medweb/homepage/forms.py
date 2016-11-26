import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from medweb.homepage.models import Person, Evaluation


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'position', 'home_phone', 'office_phone')


class EvaluationForm(ModelForm):
    # "11/25/2016 3:59 PM" is what we will receive
    call_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], required=False)

    class Meta:
        model = Evaluation
        exclude = ('person',) # Check the relevant view to see why.
        # We update/create person depending on which form is submitted via ajax

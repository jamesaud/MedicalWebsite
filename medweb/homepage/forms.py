import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from medweb.homepage.models import Person, Evaluation
from parsley.decorators import parsleyfy
from forms import NoColonForm, AutoPlaceholderForm



@parsleyfy
class PersonForm(NoColonForm, AutoPlaceholderForm, ModelForm):
    excluded_placeholder_fields = {'position'} # Fields to exclude from automatic placeholder generation

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'position', 'home_phone', 'office_phone')

        widgets = {'position': forms.TextInput(attrs={'placeholder': 'Title or Position'}), }
        parsley_namespace = 'data-parsley'


@parsleyfy
class EvaluationForm(NoColonForm, AutoPlaceholderForm, ModelForm):
    # "11/25/2016 3:59 PM" is what we will receive
    call_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'], required=False)


    class Meta:
        model = Evaluation
        exclude = ('person',) # We update/create person depending on which form is submitted via ajax
        parsley_namespace = 'data-parsley'

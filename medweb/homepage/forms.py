from django import forms
from django.forms import ModelForm

from medweb.homepage.models import Person


class person_form(ModelForm):
    model = Person
    fields = ('first_name', 'last_name')

from django import forms
from django.forms import ModelForm

from medweb.homepage.models import Person, Evaluation


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'position', 'home_phone', 'office_phone')


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields = ('__all__')

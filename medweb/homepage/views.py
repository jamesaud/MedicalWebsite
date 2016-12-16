import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from medweb.homepage.forms import PersonForm, EvaluationForm
from medweb.homepage.models import Person
from config.settings.common import HOME_PASSWORD
from medweb.homepage.models import Person, Evaluation
from functools import wraps  # Calling wraps inside a decorator keeps the docstring of the original function
# https://docs.python.org/2/library/functools.html

"""
A decorator which passes the contact form (Person form + Evaluation form) to a function
How to use: Give your function a parameter "context", the decorator provides the intial context with the forms.

"""
def pass_contact_form(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        context = {'person_form': PersonForm(), 'evaluation_form' : EvaluationForm()}
        return view(context=context, *args, **kwargs,)
    return wrapper



@pass_contact_form
def index(request, context):
    if HOME_PASSWORD == request.session.get('password'):
        return render(request, 'pages/home.html', context=context)

    elif request.method == "POST":
        if request.POST.get('password') == HOME_PASSWORD:
            request.session['password'] = request.POST.get('password')
            return render(request, 'pages/home.html', context=context)

        else:
            message = "Password Was Incorrect. Please Try Again."
            return render(request, 'pages/homepage_login.html', context={'message': message})


    return render(request, 'pages/homepage_login.html', context={})

@pass_contact_form
def test(request, context):
    return render(request, 'pages/test.html', context=context)

@pass_contact_form
def about(request, context):
    return render(request, 'pages/about.html', context=context)

@pass_contact_form
def invest(request, context):
    return render(request, 'pages/invest.html', context=context)

def compare(request):
    return render(request, 'pages/table.html', context={})

def create(request):
    if request.method == 'POST':
        post = request.POST.copy() # Copying makes the dict Mutable
        response_data = {'status': "error"}

        if request.POST.getlist('referral'):
            post['referral'] = ", ".join(request.POST.getlist('referral'))

        pform = PersonForm(post)
        eform = EvaluationForm(post)

        # Save the person object based on the form fields
        if pform.is_valid():
            person = Person(**pform.cleaned_data) # Unpack cleaned data dictionary into Person
            person.save()
            request.session['person_id'] = person.id  # Set a cookie with the associated person_id
            response_data = {'status': "success"}

        person_id = request.session.get('person_id') # Must come after cookie is set
        post['person'] = person_id  # Add the person_id to post data so eform is valid

        # Update current person OR create new one
        if eform.is_valid() and person_id:
            # Prevent empty form fields from overwriting existing evaluation object fields
            valid_clean_fields = {key: value for key, value in eform.cleaned_data.items() if value}

            # Check Django documentation on get_or_create - it returns a tuple
            evaluation, create = Evaluation.objects.get_or_create(pk=person_id,\
                                                 defaults={'person': Person.objects.get(pk=person_id)})

            for field, value in valid_clean_fields.items():
                setattr(evaluation, field, value)

            evaluation.save()
            response_data = {'status': "success"}

        return JsonResponse(response_data)

    else:
        response_data = {"status": "error"}
        return JsonResponse(response_data)

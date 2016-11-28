import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from medweb.homepage.forms import PersonForm, EvaluationForm
from medweb.homepage.models import Person
from config.settings.common import HOME_PASSWORD
from medweb.homepage.models import Person, Evaluation


def index(request):
    if HOME_PASSWORD == request.session.get('password'):
        return render(request, 'pages/home.html', context={})

    elif request.method == "POST":
        if request.POST.get('password') == HOME_PASSWORD:
            request.session['password'] = request.POST.get('password')
            return render(request, 'pages/home.html', context={})


        else:
            message = "Password Was Incorrect. Please Try Again."
            return render(request, 'pages/homepage_login.html', context={'message': message})

    return render(request, 'pages/homepage_login.html', context={})

def test(request):
    return render(request, 'pages/test.html', context={})


def about(request):
    return render(request, 'pages/about.html', context={})


def invest(request):
    return render(request, 'pages/invest.html', context={})

def compare(request):
    return render(request, 'pages/compare.htm', context={})


def create(request):
    if request.method == 'POST':
        post = request.POST.copy() # Copying makes the dict Mutable
        response_data = {'status': "error"}

        print(request.POST.getlist('referral'))
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
            print("EVALUATION SAVEd", evaluation, evaluation.call_time)
            response_data = {'status': "success"}

        return JsonResponse(response_data)

    else:
        response_data = {"status": "error"}
        return JsonResponse(response_data)

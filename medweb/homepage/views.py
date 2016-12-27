import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from medweb.homepage.forms import PersonForm, EvaluationForm, EmailForm
from medweb.homepage.models import Person
from config.settings.common import HOME_PASSWORD
from medweb.homepage.models import Person, Evaluation
from functools import wraps  # Calling wraps inside a decorator keeps the docstring of the original function
# Mailchimp imports
from utilities.mailchimp_wrapper.chimp import Client
from config.settings.common import MAILCHIMP_API_KEY, MAILCHIMP_LIST_NEWSLETTER_ID, MAILCHIMP_LIST_REPORT_ID, \
                                   MAILCHIMP_USERNAME, MAILCHIMP_DATA_CENTER

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

"""
Explanation: A decorator which passes the contact form (Person form + Evaluation form) to a function
How to use: Give your function a parameter "context", the decorator provides the intial context with the forms.
Improve: Don't require a context variable, update the context after the fact.
"""
def pass_contact_form(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        context = {'person_form': PersonForm(), 'evaluation_form' : EvaluationForm()}
        return view(context=context, *args, **kwargs,)
    return wrapper

@pass_contact_form
def index(request, context):
    context['email_form'] = EmailForm()  # Add the email form

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

@pass_contact_form
def compare(request, context):
    return render(request, 'pages/table.html', context=context)

def submit_newsletter(request):
    """
    Subscribes an email to mailchimp initial email, and optionally to the mailchimp newsletter.
    """
    response = {'status': 'error'}

    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        print('post')
        if email_form.is_valid():
            c = Client(MAILCHIMP_API_KEY, MAILCHIMP_USERNAME, MAILCHIMP_DATA_CENTER)
            email = email_form.cleaned_data.get('email')
            report_response = c.subscribe_user(MAILCHIMP_LIST_REPORT_ID, email)

            if request.POST.get('newsletter'):
                newsletter_response = c.subscribe_user(MAILCHIMP_LIST_NEWSLETTER_ID, email)
                logger.debug('Subscribed :{0}\nReport Response: {1}\nNewsletter Response: {2}\n\n'\
                             .format(email, report_response, newsletter_response))

            response['status'] = 'success'
            response['report_response'] = report_response
            response['newsletter_response'] = newsletter_response

    return JsonResponse(response)

def create(request):
    """
    Creates a user or/and evaluation.
    This is sequentially saved via ajax calls.
    The user id is saved as a cookie, which is use in subsequent ajax calls.
    If a user does not exist, it is created. If it does exist, it is updated.
    :return: JsonResponse, signifying success or failure
    """
    if request.method == 'POST':
        post = request.POST.copy() # Copying makes the dict Mutable
        response_data = {'status': "error"}

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

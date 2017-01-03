import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from medweb.homepage.forms import PersonForm, EvaluationForm, EmailForm, RandomReferralForm
from config.settings.common import HOME_PASSWORD
from medweb.homepage.models import Person, Evaluation, RandomReferral
from functools import wraps  # Calling wraps inside a decorator keeps the docstring of the original function
from medweb.homepage.view_helpers.views_form_helpers import handle_email_form
from config.settings.common import MAILCHIMP_LIST_REPORT_ID, MAILCHIMP_LIST_CHART_ID

def pass_contact_form(view):
    """
    Explanation: A decorator which passes the contact form (Person form & Evaluation form) to a function
    How to use: Give your function a parameter "context", the decorator provides the intial context with the forms.
    Improve: Don't require a context variable, update the context after the fact. Prevents refactoring the view.
    """
    @wraps(view)
    def wrapper(*args, **kwargs):
        context = {'person_form': PersonForm(), 'evaluation_form' : EvaluationForm()}
        return view(context=context, *args, **kwargs)
    return wrapper


@pass_contact_form
def index(request, context):
    context['email_form'] = EmailForm()
    context['random_referral_form'] = RandomReferralForm()

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
    context['email_form'] = EmailForm()
    context['random_referral_form'] = RandomReferralForm()
    return render(request, 'pages/table.html', context=context)


def submit_newsletter(request):
    """
    Subscribes an email to mailchimp initial email, and optionally to the mailchimp newsletter.
    :return: JsonResponse, a json response containing the outcome for each form, and the status of the view.
    """
    response = {'status': 'error'}

    if request.method == 'POST':
        email_form, report_response, newsletter_response = handle_email_form(request, MAILCHIMP_LIST_REPORT_ID)
        if email_form.is_valid():
            response['status'] = 'success'
            response['report_response'] = report_response
            response['newsletter_response'] = newsletter_response

    return JsonResponse(response)


def submit_chart(request):
    """
    Subscribes an email to mailchimp initial email, and optionally to the mailchimp newsletter.
    :return: JsonResponse, a json response containing the outcome for each form, and the status of the view.
    """
    response = {'status': 'error'}

    if request.method == 'POST':
        email_form, report_response, newsletter_response = handle_email_form(request, MAILCHIMP_LIST_CHART_ID)
        if email_form.is_valid():
            response['status'] = 'success'
            response['report_response'] = report_response
            response['newsletter_response'] = newsletter_response

    return JsonResponse(response)


def submit_referral(request):
    """
    Saves the random referral to the database.
    Improve: Only allow submissions if cookies are enabled to prevent someone from spamming the database.
    :param request: request
    :return: JsonResponse, containing the status of the response.
    """
    response = {'status': 'error'}

    if request.method == 'POST':
        referral_form = RandomReferralForm(request.POST)
        if referral_form.is_valid() and not request.session.get('referred'):
            referral = RandomReferral(**referral_form.cleaned_data)
            referral.save()
            response = {'status': 'success'}
            request.session['referred'] = True  # We don't want anyone spamming referrals.

    return JsonResponse(response)

def create(request):
    """
    Creates a user or/and evaluation.
    This is sequentially saved via ajax calls.
    The person is create first, and the person id is saved as a cookie which is use in subsequent ajax calls.
    If an evaluation does not exist, it is created. If it does exist, it is updated.
    :return: JsonResponse, signifying success or failure
    """
    response_data = {'status': "error"}

    if request.method == 'POST':
        post = request.POST.copy() # Copying makes the dict Mutable

        pform = PersonForm(post)
        eform = EvaluationForm(post)

        # Save the person object based on the form fields.
        if pform.is_valid():
            person = Person(**pform.cleaned_data)     # Unpack cleaned data dictionary into Person
            person.save()
            request.session['person_id'] = person.id  # Set a cookie with the associated person_id
            response_data = {'status': 'success'}
        else:
            response_data['person_form'] = pform.errors

        person_id = request.session.get('person_id')  # Must come after cookie is set
        post['person'] = person_id                    # Add the person_id to post data so eform is valid

        # Update current person OR create new one
        if eform.is_valid() and person_id:

            # Remove empty form fields to prevent overwriting existing evaluation object fields
            valid_clean_fields = {key: value for key, value in eform.cleaned_data.items() if value}

            # get_or_create returns a tuple
            evaluation, _ = Evaluation.objects.get_or_create(pk=person_id,\
                                                 defaults={'person': Person.objects.get(pk=person_id)})

            for field, value in valid_clean_fields.items():
                setattr(evaluation, field, value)

            evaluation.save()
            response_data = {'status': "success"}
        else:
            response_data['evaluation_form'] = eform.errors

    return JsonResponse(response_data)

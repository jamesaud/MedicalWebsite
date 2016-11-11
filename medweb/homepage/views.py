from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from config.settings.secrets import HOME_PASSWORD

from medweb.homepage.models import Person

import json


def index(request):
    if HOME_PASSWORD == request.COOKIES.get('password'):
        return render(request, 'pages/home.html', context={})

    elif request.method == "POST":
        if request.POST.get('password') == HOME_PASSWORD:
            response = render(request, 'pages/home.html', context={})
            response.set_cookie('password', request.POST.get('password'))
            return response

        else:
            message = "Password Was Incorrect. Please Try Again."
            return render(request, 'pages/homepage_login.html', context={'message': message})

    return render(request, 'pages/homepage_login.html', context={})

def test(request):
    return render(request, 'pages/test.html', context={})


def about(request):
    return render(request, 'pages/about.html', context={})

def create(request):
    if request.method == 'POST':
        post_text = request.POST.get('form')
        response_data = {}

        dict_json = json.loads(post_text)
        print(dict_json['first_name'])
        #person = Person(first_name="test", last_name="test")
       # person.save()

        response_data['result'] = 'Create post successful!'
        #response_data['first_name'] = person.first_name


        return JsonResponse(response_data)
    else:
        response_data = {"nothing to see": "this isn't happening"}
        return JsonResponse(response_data)

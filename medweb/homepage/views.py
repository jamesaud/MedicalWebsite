from django.shortcuts import render
from config.settings.secrets import HOME_PASSWORD


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
    print("----test------")
    return render(request, 'pages/test.html', context={})

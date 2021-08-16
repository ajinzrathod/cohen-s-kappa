from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.conf import settings as django_settings


# Create your views here.


@login_required
def home(request):
    data = {
        'active_page': 'home',
    }
    return render(request, 'home.html', data)


def error_404(request):
    return render(request, 'error-pages/error-404.html')


def error_403(request):
    return render(request, 'error-pages/error-403.html')


def error_500(request):
    return render(request, 'error-pages/error-500.html')


def tos(request):
    return render(request, 'terms-and-policy/terms-of-service.html')


def privacy_policy(request):
    return render(request, 'terms-and-policy/privacy-policy.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect(django_settings.LOGIN_REDIRECT_URL)


def login(request):
    # go to url / instead of home.html
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'account/login.html')

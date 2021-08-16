from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.conf import settings as django_settings


# Create your views here.


@login_required
def tweetsHome(request):
    data = {
        'active_page': 'tweets',
    }
    return render(request, 'tweets/index.html', data)

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.conf import settings as django_settings
from django.utils.translation import activate
from .models import Response, Tweet

# Create your views here.


@login_required
def tweetsHome(request):
    # data = {
    #    'active_page': 'tweets',
    # }
    data = Response.objects.all()
    return render(request,
                  'tweets/index.html',
                  {'data': data, 'active_page': 'tweets'})

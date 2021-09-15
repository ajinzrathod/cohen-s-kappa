from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import admin_required


# Create your views here.
@login_required
@admin_required
def compareHome(request):
    data = {
        'active_page': 'compare',
    }
    return render(request, 'compare/index.html', data)

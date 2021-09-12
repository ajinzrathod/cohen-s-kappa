from django.shortcuts import render

# Create your views here.

def contactHome(request):
    # data = Response.objects.all()    {'data': data }
    return render(request, "contact/index.html")
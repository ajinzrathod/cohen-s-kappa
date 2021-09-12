from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.


def contactHome(request):
    # data = Response.objects.all()    {'data': data }

    user = request.user
    form = ContactForm(instance=user)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/contact/success/')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, "contact/index.html", context)


def contactFormSuccess(request):
    return render(request, "contact/success.html")
    

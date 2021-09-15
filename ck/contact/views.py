from django.shortcuts import render, redirect
from .forms import ContactForm
# from django.contrib.auth.models import User
# Create your views here.


def contactHome(request):
    form = ContactForm(instance=request.user)

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

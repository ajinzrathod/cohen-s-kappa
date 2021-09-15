# forms.py
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [ 'issue', 'issue_image']
        help_texts = {
            'issue': _('Briefly explain what happened or what\'s  not working '),
        }
        widgets = {
            'issue': Textarea(attrs={'cols': 80, 'rows': 3}),
        }
    # fields = '__all__'

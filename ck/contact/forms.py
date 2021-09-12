# forms.py
from django import forms
from .models import *


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [ 'issue', 'issue_image']
        
    # fields = '__all__'

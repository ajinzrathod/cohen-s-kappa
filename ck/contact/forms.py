# forms.py
from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _
from django.forms import Textarea


class ContactForm(forms.ModelForm):
    issue = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Explain your issue here',
        }
    ))

    class Meta:
        model = Contact
        fields = ['issue', 'issue_image']
        help_texts = {
            'issue': _(
                'Briefly explain what happened or what\'s  not working'),
        }
        widgets = {
            'issue': Textarea(attrs={'cols': 80, 'rows': 3}),
        }

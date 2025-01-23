# forms.py
from django import forms
from .models import ContactDb

from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-success shadow-sm'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control border-success shadow-sm'
    }))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-success shadow-sm'
    }))
    objective = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-success shadow-sm'
    }))
    Message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control border-success shadow-sm'
    }))

# forms.py
from django import forms
from .models import ContactDb

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDb
        fields = ['Name', 'email', 'phone_no', 'objective', 'Message']

    Name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter name',
            'pattern': '^[a-zA-Z\s]+$',
            'title': 'Name should only contain alphabets and whitespaces',
            'class': "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm p-4 h-10"
        })
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'placeholder': 'Enter email',
            'title': 'Enter a valid email id',
            'class': "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm p-4 h-10",
        })
    )
    
    phone_no = forms.CharField(
        label='Phone Number',
        max_length=10,
        widget=forms.TextInput(attrs={
            'pattern': '^[0-9]{10}$',
            'placeholder': 'Enter phone number',
            'title': 'The contact number must be exactly 10 digits.',
            'class': "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm p-4 h-10"
        })
    )
    
    objective = forms.ChoiceField(
        label='Objective',
        choices=[
            ('Select_objective', 'Select Objective'),
            ('weight_loss', 'Weight Loss'),
            ('weight_gain', 'Weight Gain'),
            ('maintain_strength', 'Maintain Weight and Build Strength')
        ],
        widget=forms.Select(attrs={'class': 'form-select p-3 rounded-lg w-full'})
    )
    
    Message = forms.CharField(
        label='Message',
        max_length=300,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter message or queries.',
            'class': "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm p-4 h-10"
        })
    )

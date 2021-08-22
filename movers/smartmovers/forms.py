from django import forms
from .models import Rating,sms

class RateForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ['rate','comment']

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = sms
        fields = ['name','message']
from django import forms
from django.forms import fields
from .models import BillingAddress
class BillingForm(forms.ModelForm):
    class Meta:
        model=BillingAddress
        fields=['address','zipcode','city','country']
from django.forms import ModelForm
from django import forms
from .models import Order
from django.forms.widgets import NumberInput


class OrderForm(ModelForm):

    start_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = [

            'brand',
            'start_date',
            'end_date',
        ]


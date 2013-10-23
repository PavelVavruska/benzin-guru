import datetime
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import GasPrice


class GasPriceForm(ModelForm):
    date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today)

    class Meta:
        model = GasPrice
        fields = ['station', 'date', 'price']
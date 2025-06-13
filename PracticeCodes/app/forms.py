from django import forms
from .models import App

class NameForm(forms.Form):
    name_variety= forms.ModelChoiceField(queryset=App.objects.all(), label='Select Variety')
from django import forms
from django.forms.fields import EmailField

class Apply(forms.Form):
    file = forms.FileField(required=False)

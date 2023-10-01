from django.core import validators
from django import forms


def start_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name must start with S')


class UserForm(forms.Form):
    name = forms.CharField(validators=[start_s])
    email = forms.CharField()
    password = forms.CharField()

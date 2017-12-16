from django import forms
from .models import Token


class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['name', ]

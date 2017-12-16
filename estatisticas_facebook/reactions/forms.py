from django import forms
from .models import Reaction


class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['name', ]

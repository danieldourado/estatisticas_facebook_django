from django import forms
from .models import Paging


class PagingForm(forms.ModelForm):
    class Meta:
        model = Paging
        fields = ['name', ]

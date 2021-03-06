from django import forms
from .models import Page

class PageCreateForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'name',
            'access_token',
            ]
            
class PageInsightsCreateForm(forms.Form):
    since = forms.DateField()
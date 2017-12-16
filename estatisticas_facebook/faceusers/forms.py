from django import forms
from .models import FaceUsers


class FaceUsersForm(forms.ModelForm):
    class Meta:
        model = FaceUsers
        fields = ['name', ]

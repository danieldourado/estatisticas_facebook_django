from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', ]

class PostCreateForm(forms.Form):
    access_token = forms.CharField()
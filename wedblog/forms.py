from django import forms
from .models import Wedblog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Wedblog
        fields = ['title','body']


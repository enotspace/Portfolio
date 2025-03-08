from django import forms
from .models import formmodel

class formform(forms.ModelForm):
    class Meta:
        model = formmodel
        fields = ('first_name','last_name','text')
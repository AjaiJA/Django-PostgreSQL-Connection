from django import forms
from djanpost.models import LogIn

class LogInForm(forms.ModelForm):
    class Meta:
        model=LogIn
        fields="__all__"

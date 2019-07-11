from django import forms
from .models import Login


class FormName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = "__all__"

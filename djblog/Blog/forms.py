from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'name', 'placeholder': 'your name'})
        self.fields['email'].widget.attrs.update({'id': 'email', 'placeholder': 'email'})
        self.fields['password'].widget.attrs.update({'id': 'pass', 'placeholder': 'password'})
        self.fields['telephone'].widget.attrs.update({'id': 'telephone', 'placeholder': 'telephone'})


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'name', 'placeholder': 'your name'})
        self.fields['password'].widget.attrs.update({'id': 'pass', 'placeholder': 'password'})

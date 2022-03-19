import re
from django import forms
from .models import *
# phone number imports
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# auth import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'id': 'pass', 'type': 'password', 'placeholder': 'confirm password'}),
    )

    telephone = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
        label="Phone number",
        required=False,
        #initial='EG',
    )

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'id': 'name', 'placeholder': 'your name'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'email'}),
            'password': forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'password', 'type': 'password'}),
            # 'telephone': PhoneNumberField(
            #     widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
            #     label="Phone number",
            #     required=False,
            #     initial='EG',
            # )
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        telephone = cleaned_data.get("telephone")

        # validate username
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError(
                "That user is already taken , please select another ")
        elif not re.search(r'^\w+$', username):
            raise forms.ValidationError(
                "Username can only contain alphanumeric characters and the underscore.")

        # validate password
        if password1 != password2:
            raise forms.ValidationError("Your current and confirm password do not match.")

        # validate telephone number
        # tel_pattern = r'^01[0-2,5]{1}[0-9]{8}$'
        # if not re.match(tel_pattern, telephone):
        #     raise forms.ValidationError("invalid telephone number")
        # return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'name', 'placeholder': 'your name'})
        self.fields['password'].widget.attrs.update({'id': 'pass', 'placeholder': 'password'})

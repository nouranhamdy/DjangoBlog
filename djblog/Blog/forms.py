import re
from django import forms
from .models import *
# phone number imports
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# auth import
from django.contrib.auth.forms import UserCreationForm
from .models import user


class RegisterForm(UserCreationForm):
    # password2 = forms.CharField(
    #     label="Confirm password",
    #     widget=forms.PasswordInput(
    #         attrs={'id': 'pass', 'type': 'password', 'placeholder': 'confirm password'}),
    # )

    # telephone = PhoneNumberField(
    #     widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
    #     label="Phone number",
    #     required=False,
    #     #initial='EG',
    # )

    class Meta:
        model = user
        fields = ('username', 'email', 'first_name', 'last_name', 'telephone', 'password1', 'password2')
        # fields = ('username', 'email', 'password')
        # widgets = {
        #     'username': forms.TextInput(attrs={'id': 'name', 'placeholder': 'your name'}),
        #     'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder': 'password', 'type': 'password'}),
        #     # 'telephone': PhoneNumberField(
        #     #     widget=forms.TextInput(attrs={'placeholder': 'Phone'}),
        #     #     label="Phone number",
        #     #     required=False,
        #     #     initial='EG',
        #     # )
        # }

    # def clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     username = cleaned_data.get("username")
    #     email = cleaned_data.get("email")
    #     password1 = cleaned_data.get("password")
    #     # password2 = cleaned_data.get("password2")
    #     # telephone = cleaned_data.get("telephone")
    #
    #     # validate username
    #     user = User.objects.filter(username=username)
    #     if user:
    #         raise forms.ValidationError(
    #             "That user is already taken , please select another ")
    #     elif not re.search(r'^\w+$', username):
    #         raise forms.ValidationError(
    #             "Username can only contain alphanumeric characters and the underscore.")
    #
    #     # validate password
    #     # if password1 != password2:
    #     #     raise forms.ValidationError("Your current and confirm password do not match.")
    #
    #     #validate telephone number
    #     # tel_pattern = r'^01[0-2,5]{1}[0-9]{8}$'
    #     # if not re.match(tel_pattern, telephone):
    #     #     raise forms.ValidationError("invalid telephone number")
    #     return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'name', 'placeholder': 'your name'})
        self.fields['password'].widget.attrs.update({'id': 'pass', 'placeholder': 'password'})


choices = Category.objects.all().values_list('name','name')
choice_list= []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
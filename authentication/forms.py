from django import forms

from django.core.validators import ValidationError


def validate_file_extension(value):
    if not (value.content_type == "image/png" or value.content_type == "image/jpeg"):
        raise ValidationError("Invalid file Type, only png, jpg or jpeg")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    re_enter_password = forms.CharField(max_length=64, widget=forms.PasswordInput)
    picture = forms.FileField(required=False, validators=[validate_file_extension])

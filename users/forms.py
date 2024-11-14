from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordResetForm,
)

from .models import MailingUser


class MailingUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15, required=True, help_text="Введите ваш номер телефона."
    )
    username = forms.CharField(max_length=50, required=True, help_text="Псевдоним")
    country = forms.CharField(
        max_length=20, required=True, help_text="Страна проживания"
    )

    class Meta:
        model = MailingUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "country",
            "password1",
            "password2",
        )


class MailingUserChangeForm(UserChangeForm):
    class Meta:
        model = MailingUser
        fields = (
            "username",
            "avatar",
            "first_name",
            "last_name",
            "phone_number",
            "country",
        )


class MailingUserPassRestore(PasswordResetForm):
    class Meta:
        model = MailingUser
        fields = ("email",)

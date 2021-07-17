from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    name = forms.CharField(
        label='Почта',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control input-lg'}),
    )

    email = forms.CharField(
        label='Почта',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control input-lg'}),
    )
    password = forms.CharField(
        label='Пароль',
        max_length=128,
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control input-lg'}),
    )
    login = forms.CharField(
        label='Пароль',
        max_length=128,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control input-lg'}),
    )
    def clean_email(self):
        login = self.cleaned_data.get('login')

        if not login:
            raise ValidationError('Обязательное поле')

        return login

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not password:
            raise ValidationError('Обязательное поле')

        return password
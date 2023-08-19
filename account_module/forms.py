from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterFrom(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری'
        }),
    )
    email = forms.EmailField(
        label='آدرس ایمیـل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'آدرس ایمیـل'
        }),
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور'
        }),

    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار کلمه عبور'
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور با تکرار کلمه عبور برابر نیست')


class LoginForm(forms.Form):
    email = forms.CharField(
            label='آدرس ایمیـل یا نام کاربری',
            widget=forms.TextInput(attrs={
                'placeholder': 'آدرس ایمیـل یا نام کاربری'
            }),
        )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور'
        }),

    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
            label='آدرس ایمیـل',
            widget=forms.EmailInput(attrs={
                'placeholder': 'آدرس ایمیـل'
            }),
        )


class ResetPasswordFrom(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'کلمه عبور'
        }),

    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار کلمه عبور'
        })
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور با تکرار کلمه عبور برابر نیست')

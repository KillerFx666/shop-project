from django import forms
from .models import ContactUS


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = ['full_name', 'email', 'title', 'massage']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضـوع'
            }),
            'massage': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'پیغـام شمـا',
                'rows': '8',
                'id': 'message'
            }),
        }
        # labels = {
        #     'full_name': 'نام و نام خانوادگی',
        #     'email': 'ایمیل'
        # }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید'
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد کنید'
            }
        }



from django import forms
from .models import Contactform
from django.contrib.auth.models import User
class contact_form(forms.ModelForm):
    class Meta:
        model=Contactform
        fields = ['name','email','phone_number', 'description']
        widgets={
            'name':forms.TextInput(attrs={'class': 'box', 'placeholder': 'نام شما'})
            ,'email':forms.EmailInput(attrs={'class': 'box', 'placeholder': 'ایمیل شما'})
            ,'phone_number':forms.TextInput(attrs={'class': 'box', 'placeholder': 'شماره همراه'})
            , 'description':forms.Textarea(attrs={'class': 'box', 'placeholder': 'پیام شما', 'cols': 30, 'rows': 10})

        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) # کاربر را از آرگومان‌ها بگیرید
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['name'].initial = user.username # مقدار اولیه نام را تنظیم کنید
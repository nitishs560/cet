from django import forms
from .models import student
from phone_field import PhoneField


class UserRegisterForm:
    first_name = forms.CharField(label='first_name',max_length=20,help_text='First Name')
    last_name = forms.CharField(label='last_name',max_length=20,help_text='Last Name')
    address = forms.CharField(label='address',help_text='Address',max_length=100)
    email = forms.EmailField(label='email',help_text='email@gmail.com')
    phone_no = forms.CharField(label='phone_no',help_text='Phone No.')

    class Meta:
        model = student
        fields = ['first_name','last_name','address','email','phone_no']


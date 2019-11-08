from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()




class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    # check = forms.BooleanField(required = True,label='Terms and conditions')
   
    class Meta:
        model = User
        fields = ('username','email','phone','password1', 'password2')
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('This email address is already registered.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and User.objects.filter(phone=phone).count() > 0:
            raise forms.ValidationError('This phone number is already registered.')
        return phone

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password')





class StartForm(forms.Form):
    username= forms.CharField(max_length=254, required=True,)
   
        

    
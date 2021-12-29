from django .forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        Fields = ['userneme','email', 'first_name','last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        Fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2',]


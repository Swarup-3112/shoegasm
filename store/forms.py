from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import cart


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1']


class addtocart(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'
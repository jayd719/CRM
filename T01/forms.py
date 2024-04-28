from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class UserReg(UserCreationForm):
    addr = forms.CharField(required=True)
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['email','addr']
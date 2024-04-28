from django.shortcuts import render,HttpResponse
from django import forms
from django_recaptcha.fields import ReCaptchaField,ReCaptchaV2Checkbox

# Create your views here.

class ContactForm(forms.Form): 
    email = forms.CharField(max_length=100)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    
def landingPage_1(requests):
   
          
    return render(requests, 'homepage.html')

def projects(requests):
    return render(requests,'projects.html')
    
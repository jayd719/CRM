from django.shortcuts import render
from serverJSP.settings import COMPANYNAME
from .models import PythonLibs 
from .models import CNC
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def main(requests):
    DATA={
    'companyName':COMPANYNAME,
    'pythonLibs': PythonLibs.objects.all(),
    'machines':CNC.objects.all()
}   
    
    return render(requests,f'components/homepage.html',DATA)


def loginPage(requests):
    return render(requests,'components/loginpage.html')
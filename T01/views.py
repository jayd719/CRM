from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserReg


def main(requests):
    return render(requests,f'components/homepage.html')


def addToEmailList(requests):
    context = {'form':UserReg(),'title':'Create Account'}   
    if requests.method=="POST":
            form = UserReg(requests.POST)
            if form.is_valid():
                print(form)
                return redirect('home-main')
                
    else:
        form = UserReg()

    return render(requests,f'components/homepage.html',context)

def loginPage(requests):
    return render(requests,'components/loginpage.html')
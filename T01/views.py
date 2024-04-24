from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main(requests):
    return render(requests,f'components/homepage.html')


def loginPage(requests):
    return render(requests,'components/loginpage.html')
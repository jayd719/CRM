from django.urls import path,include
from .views import main,loginPage
urlpatterns = [
    path('',main,name='home-main'),
    path('login/',loginPage,name='login')
    
]

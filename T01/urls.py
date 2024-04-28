from django.urls import path,include
from .views import main,loginPage
from .views import addToEmailList
urlpatterns = [
    path('',main,name='home-main'),
    path('login/',loginPage,name='login'),
    path('addToEmailList/',addToEmailList,name='record-URL')
    
]

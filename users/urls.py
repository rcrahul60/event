from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('register/',RegistrationView,name="registerView"),
    path('login/',login,name="login"),
   

]
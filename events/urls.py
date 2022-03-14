from django.urls import path,include
from .views import *

urlpatterns = [
    path('list/',EventListView,name="eventList"),
    path('create/',EventCreateView,name="eventCreate"),
    path('update/<int:id>/',EventUpdateView,name="eventUpdate"),
    path('home/',index,name="home")

    
   

]
from django.urls import path,include
from .views import *

urlpatterns = [
    path('list/',EventListView,name="eventList"),
    path('create/',EventCreateView,name="eventCreate"),
    path('update/<int:id>/',EventUpdateView,name="eventUpdate"),
    path('booking/',EventBookingView,name="eventBooking"),
    path('booking/list/',EventBookingList,name="eventBookingList"),



    
   

]
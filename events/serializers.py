from .models import *
from rest_framework import serializers
from django.conf import settings



#Event Serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields='__all__'


#Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingCart
        fields = '__all__'

    
from django.db import models
from django.utils import timezone
from users.models import *
from django.utils.translation import gettext_lazy as _


#Event
class Event(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True,verbose_name=_("Event Name"),unique=True)
    location = models.CharField(max_length=250,null=True,blank=True,verbose_name=_("Location"))
    summary = models.TextField(max_length=500,null=True,blank=True,verbose_name=_("Summary"))
    seats = models.PositiveIntegerField(default=0,verbose_name=_("Seats"))
    ticket_amount = models.FloatField(default=0,verbose_name=_("Ticket Amount"))
    created_by = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,related_name="created_by",verbose_name=_("Created By"),blank=True,null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'event'



#Booking 
class BookingCart(models.Model):
    BOOKING_STATUS = (
        (1,'Pending'),
        (2,'Completed')
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_("User Id"),blank=True,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,verbose_name=_("Event Id"),blank=True,null=True)
    ticket_quantity = models.PositiveIntegerField(default=0,verbose_name=_("Ticket Quantity"))
    total_price = models.FloatField(default=0.00,verbose_name=_("Total Price"))
    status = models.PositiveSmallIntegerField(choices=BOOKING_STATUS,default=1)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = 'event_booking_cart'
from django.contrib import admin
from .models import Menu, Booking
from rest_framework.authtoken.models import Token

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    search_fields = ('title',)
    list_filter = ('price',)
    ordering = ('id',)



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date')
    search_fields = ('name',)
    list_filter = ('no_of_guests',)
    ordering = ('id',)


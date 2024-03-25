from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking, Table


# Register your models here.

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = (
        'name', 'email', 'party_size', 'session_length', 'start_time',
        'date', 'table'
    )
    search_fields = ['name']


# Register Table model with the admin site
admin.site.register(Table)

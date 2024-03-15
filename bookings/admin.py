from django.contrib import admin
from .models import Booking, Table
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'email', 'party_size', 'session_length', 'start_time', 'date', 'table')
    search_fields = ['name']

# Register your models here.

admin.site.register(Table)
from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('name', 'event_date', 'event_time', 'status')
    search_fields = ['name']
    list_filter = ('status',)
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)
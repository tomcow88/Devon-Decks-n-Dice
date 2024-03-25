from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Comment


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    list_display = (
        'name', 'event_date', 'event_time', 'status'
    )
    search_fields = ['name']
    list_filter = ('status',)
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Comment)

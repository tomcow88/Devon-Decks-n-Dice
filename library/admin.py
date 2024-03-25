from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BoardGame

# Register your models here.


@admin.register(BoardGame)
class BoardGameAdmin(SummernoteModelAdmin):

    list_display = ('name', 'bgg_id', 'year_published', 'status')
    search_fields = ['name']
    list_filter = ('status',)

from django.contrib import admin
from .models import BoardGame
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(BoardGame)
class BoardGameAdmin(SummernoteModelAdmin):

    list_display = ('name', 'bgg_id', 'year_published', 'min_players', 'max_players', 'playing_time', 'age', 'image', 'thumbnail', 'description', 'status')
    search_fields = ['name']

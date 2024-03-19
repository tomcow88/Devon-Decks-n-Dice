from . import views
from django.urls import path

urlpatterns = [
    path('', views.BoardGameList.as_view(), name='library'),
    path('game-search/', views.search_results, name='game_search'),
    path('add-game-to-database/', views.add_game_to_database, name='add_game_to_database'),
]

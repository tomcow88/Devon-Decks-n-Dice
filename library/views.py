from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
import requests
import xml.etree.ElementTree as ET
from .forms import SearchForm
from .models import BoardGame


class BoardGameList(generic.ListView):
    queryset = BoardGame.objects.filter(status=1).order_by('name')
    template_name = "library/boardgame_list.html"
    paginate_by = 6


def search_results(request):
    search_term = request.GET.get('query', '')
    if search_term:
        games = fetch_games(search_term)
        for game in games:
            game['is_in_library'] = BoardGame.objects.filter(
                bgg_id=game['bgg_id']).exists()
    else:
        games = []

    form = SearchForm(request.GET or None)

    paginator = Paginator(games, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'library/game_search.html', {
        'page_obj': page_obj,
        'form': form
    })


def add_game_to_database(request):
    if request.method == 'POST':
        try:
            game = BoardGame.objects.create(
                bgg_id=request.POST.get('bgg_id'),
                name=request.POST.get('name'),
                year_published=request.POST.get('year_published'),
                min_players=request.POST.get('min_players'),
                max_players=request.POST.get('max_players'),
                playing_time=request.POST.get('playing_time'),
                age=request.POST.get('age'),
                description=request.POST.get('description'),
                image=request.POST.get('image'),
                thumbnail=request.POST.get('thumbnail'),
                status=1
            )
            messages.success(request, 'Game added to library.')
        except Exception as e:
            messages.error(request, f'Failed to add the game: {str(e)}')
        return HttpResponseRedirect(reverse('game_search'))


def fetch_games(search_term):
    search_response = requests.get(
        f'https://www.boardgamegeek.com/xmlapi2/search?query={search_term}'
        '&type=boardgame')

    if search_response.status_code == 200:
        search_root = ET.fromstring(search_response.content)
        games_details = []

        for item in list(search_root)[:18]:
            bgg_id = item.get('id')

            details_response = requests.get(
                f'https://www.boardgamegeek.com/xmlapi2/thing?id={bgg_id}')
            if details_response.status_code == 200:
                details_root = ET.fromstring(details_response.content)

                for detail in details_root.findall('item'):
                    min_players = detail.find(".//minplayers").get(
                        'value') if detail.find(".//minplayers") is not None else '1'
                    max_players = detail.find(".//maxplayers").get(
                        'value') if detail.find(".//maxplayers") is not None else min_players
                    playing_time = detail.find(".//playingtime").get(
                        'value') if detail.find(".//playingtime") is not None else '0'
                    age = detail.find(".//minage").get(
                        'value') if detail.find(".//minage") is not None else '0'
                    name = detail.find(".//name[@type='primary']").get(
                        'value') if detail.find(".//name[@type='primary']") is not None else 'No Name'
                    year_published = detail.find('yearpublished').get(
                        'value') if detail.find('yearpublished') is not None else 'N/A'
                    description = detail.find("description").text if detail.find(
                        "description") is not None else 'No description'
                    image = detail.find("image").text if detail.find(
                        "image") is not None else 'No image'
                    thumbnail = detail.find("thumbnail").text if detail.find(
                        "thumbnail") is not None else 'No thumbnail'

                    game_details = {
                        'bgg_id': bgg_id,
                        'name': name,
                        'year_published': year_published,
                        'min_players': min_players,
                        'max_players': max_players,
                        'playing_time': playing_time,
                        'age': age,
                        'image': image,
                        'thumbnail': thumbnail,
                        'description': description,
                    }
                    games_details.append(game_details)
                    break

        return games_details
    return []

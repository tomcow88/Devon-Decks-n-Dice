from django.shortcuts import render
import requests

# Create your views here.

def library(request):
    response=requests.get('https://api.geekdo.com/xmlapi/search').json()
    return render(request, 'game_library.html', {'response':response})
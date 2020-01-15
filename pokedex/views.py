from django.shortcuts import render
import requests

def pokemon_search(request):
    search_result = {}
    if 'pokemon_name' in request.GET:
        name = request.GET['pokemon_name']

        url = 'https://pokeapi.co/api/v2/pokemon/%s' % name.lower()
        response = requests.get(url)
        search_success = (response.status_code == 200)
        if search_success:
            search_result = response.json()
        search_result['success'] = search_success

    return render(request, 'pokemon_search.html', {'search_result': search_result})

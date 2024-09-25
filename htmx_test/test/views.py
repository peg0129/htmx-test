from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def test(request):
    return render(request, 'index.html')

def pokemonList(request):
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
    data = response.json()

    pokemon_names = [pokemon['name'] for pokemon in data['results']]

    return JsonResponse({'pokemon_names': pokemon_names})

def pokemonDetail(request, pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # ポケモンの詳細データをHTMLで返す
        html_content = f"""
        <p>{data['name'].capitalize()}</p>
        <img src="{data['sprites']['front_default']}" alt="{data['name']}" />
        <p><strong>Height:</strong> {data['height']}</p>
        <p><strong>Weight:</strong> {data['weight']}</p>
        <p><strong>Base Experience:</strong> {data['base_experience']}</p>
        <p><strong>Abilities:</strong></p>
        <ul>
        {''.join([f"<li>{ability['ability']['name']}</li>" for ability in data['abilities']])}
        </ul>
        """
        return HttpResponse(html_content)
    else:
        return HttpResponse(f"<p>Pokemon {pokemon} not found.</p>", status=404)
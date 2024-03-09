from django.shortcuts import render
import requests
from .models import Filme

def filmes_api(request):
    url = 'http://www.omdbapi.com/?t=The Matrix&apikey=SUA_CHAVE_API'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
       
        if data.get('Response') == "True":
            filme = Filme.objects.get_or_create(
                titulo =data.get('Title',''),
                ano_lancamento =data.get('Year',''),
                diretor =data.get('Director',''),
                genero =data.get('Genre','')
            )
            context = {'filme': filme}
        else:
            context = {'error': 'Filme não encontrado'}
        
        return render(request, 'filmeapp/filmes.html', context)
    else:
        return render(request, 'filmeapp/error.html', {'error': 'Erro ao buscar o filme'})

from django.shortcuts import render
from .models import Locacao, Filme
# Create your views here.

def index(request):
    return render(request,'core/index.html')

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, 'core/locacao.html', {'locacoes': locacoes})

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'core/filmes.html', {'filmes': filmes})
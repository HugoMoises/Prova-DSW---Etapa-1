from django.shortcuts import render, get_object_or_404
from .models import Equipe, Modalidade

def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()

    context ={
        "equipes": equipes,
        "modalidades": modalidades
    }
    return render(request, 'jogos/index.html', context)

def equipe(request, id):
    equipe = get_object_or_404(Equipe, pk=id)

    context = {
        "equipe": equipe
    }

    return render(request, 'jogos/equipe.html', context)

def modalidade(request, id):
    modalidade = get_object_or_404(Modalidade, pk=id)

    context = {
        "modalidade": modalidade
    }

    return render(request, 'jogos/modalidade.html', context)
from django.shortcuts import render
from django.views.generic import DetailView
from modalidades.models import Modalidade

class ModalidadeDetailView(DetailView):
    model = Modalidade
    template_name = 'modalidades/modalidade.html'
    context_object_name = 'modalidade'

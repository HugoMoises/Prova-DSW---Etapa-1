from django.views.generic import ListView, DetailView
from .models import Equipe, Modalidade


class IndexView(ListView):
    model = Equipe
    template_name = 'jogos/index.html'
    context_object_name = 'equipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modalidades'] = Modalidade.objects.all()
        return context


class EquipeDetailView(DetailView):
    model = Equipe
    template_name = 'jogos/equipe.html'
    context_object_name = 'equipe'


class ModalidadeDetailView(DetailView):
    model = Modalidade
    template_name = 'jogos/modalidade.html'
    context_object_name = 'modalidade'

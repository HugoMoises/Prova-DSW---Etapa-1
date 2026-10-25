from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Equipe, Modalidade
from .forms import EquipeForm


class IndexView(ListView):
    model = Equipe
    template_name = 'jogos/index.html'
    context_object_name = 'equipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modalidades'] = Modalidade.objects.all()
        context['form'] =  EquipeForm()
        return context
    
class EquipeCreateView(CreateView):
    model = Equipe
    form_class = EquipeForm
    success_url = reverse_lazy('index')
    template_name = 'jogos/partials/equipe_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipes'] = Equipe.objects.all()
        context['modalidades'] = Modalidade.objects.all()
        context['abrir-modal'] = self.request.method == "POST"
        return context



class EquipeDetailView(DetailView):
    model = Equipe
    template_name = 'jogos/equipe.html'
    context_object_name = 'equipe'


class ModalidadeDetailView(DetailView):
    model = Modalidade
    template_name = 'jogos/modalidade.html'
    context_object_name = 'modalidade'

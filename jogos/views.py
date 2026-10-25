from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

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
    template_name = 'jogos/partials/equipe_form_modal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipes'] = Equipe.objects.all()
        context['modalidades'] = Modalidade.objects.all()
        context['abrir-modal'] = self.request.method == "POST"
        return context

class EquipeUpdateView(UpdateView):
    model = Equipe
    form_class = EquipeForm
    success_url = reverse_lazy('index')
    template_name = 'jogos/partials/equipe_edit_modal.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] =  EquipeForm(instance=self.object)
        return context


class ModalidadeDetailView(DetailView):
    model = Modalidade
    template_name = 'jogos/modalidade.html'
    context_object_name = 'modalidade'

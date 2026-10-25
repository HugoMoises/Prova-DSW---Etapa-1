from django import forms
from jogos.models import Equipe

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'curso', 'cor']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome da equipe',
            }),
            'curso': forms.TextInput(attrs={
                'placeholder': 'Curso',
            }),
            'cor': forms.TextInput(attrs={
                'type': 'color',
            }),
        }
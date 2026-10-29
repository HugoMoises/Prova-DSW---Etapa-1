from django.contrib import admin
from .models import Atleta

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['equipe', 'modalidade']
    search_fields = ['nome']

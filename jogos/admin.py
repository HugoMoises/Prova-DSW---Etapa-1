from django.contrib import admin
from .models import Modalidade, Equipe, Atleta, Tecnico

class TecnicoInline(admin.TabularInline):
    model = Tecnico

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['equipe', 'modalidade']
    search_fields = ['nome']

@admin.register(Equipe)
class Equipeadmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']   

    inlines = [TecnicoInline] 

admin.site.register(Modalidade)
admin.site.register(Tecnico)
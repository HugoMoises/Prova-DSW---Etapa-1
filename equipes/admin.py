from django.contrib import admin
from .models import Equipe
from tecnicos.models import Tecnico

class TecnicoInline(admin.TabularInline):
    model = Tecnico

@admin.register(Equipe)
class Equipeadmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']   

    inlines = [TecnicoInline] 

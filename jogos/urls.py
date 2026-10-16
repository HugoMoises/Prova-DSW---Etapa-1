from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('equipe/<int:id>', views.equipe, name="equipe"),
    path('modalidade/<int:id>', views.modalidade, name="modalidade")
]

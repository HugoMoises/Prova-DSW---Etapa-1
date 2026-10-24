from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('equipe/<int:pk>', views.EquipeDetailView.as_view(), name="equipe"),
    path('modalidade/<int:pk>', views.ModalidadeDetailView.as_view(), name="modalidade")
]

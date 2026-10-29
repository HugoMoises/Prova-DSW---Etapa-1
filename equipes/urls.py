from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("equipe/<int:pk>", views.EquipeDetailView.as_view(), name="equipe"),
    path('equipe/criar', views.EquipeCreateView.as_view(), name="equipe-create"),
    path('equipe/<int:pk>/editar', views.EquipeUpdateView.as_view(), name="equipe-update"),
]

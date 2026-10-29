from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.ModalidadeDetailView.as_view(), name="modalidade")
]

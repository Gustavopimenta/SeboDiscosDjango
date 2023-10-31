from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_discos, name='lista_discos'),  # Rota padrão para a página inicial
    path('lista_discos/', views.lista_discos, name='lista_discos'),
    path('detalhes_disco/<int:disco_id>/', views.detalhes_disco, name='detalhes_disco'),
]
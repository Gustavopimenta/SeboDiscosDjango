from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_discos, name='lista_discos'),  # Rota padrão para a página inicial
    path('lista_discos/', views.lista_discos, name='lista_discos'),
    path('detalhes_disco/<int:disco_id>/', views.detalhes_disco, name='detalhes_disco'),
    path('discos/cadastrar/', views.cadastrar_disco, name='cadastrar_disco'),
    path('discos/editar/<int:disco_id>/', views.editar_disco, name='editar_disco'),
    path('discos/excluir/<int:disco_id>/', views.excluir_disco, name='excluir_disco'),



]
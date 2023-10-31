from django.shortcuts import render, get_object_or_404
from .models import Disco

def lista_discos(request):
    discos = Disco.objects.all()
    return render(request, 'discos/lista_discos.html', {'discos': discos})

def detalhes_disco(request, disco_id):
    disco = get_object_or_404(Disco, pk=disco_id)
    return render(request, 'discos/detalhes_disco.html', {'disco': disco})

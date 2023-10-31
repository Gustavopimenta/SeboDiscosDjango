from django.shortcuts import render, get_object_or_404
from .models import Disco
from .forms import DiscoForm

def lista_discos(request):
    discos = Disco.objects.all()
    return render(request, 'discos/lista_discos.html', {'discos': discos})

def detalhes_disco(request, disco_id):
    disco = get_object_or_404(Disco, pk=disco_id)
    return render(request, 'discos/detalhes_disco.html', {'disco': disco})

def cadastrar_disco(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscoForm()
    return render(request, 'discos/cadastrar_disco.html', {'form': form})

def editar_disco(request, disco_id):
    disco = get_object_or_404(Disco, pk=disco_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscoForm(instance=disco)
    return render(request, 'discos/editar_disco.html', {'form': form, 'disco': disco})

def excluir_disco(request, disco_id):
    disco = get_object_or_404(Disco, pk=disco_id)
    disco.delete()
    return redirect('lista_discos')

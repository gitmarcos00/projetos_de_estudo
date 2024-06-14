from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# Create your views here.

def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) # Busca todos os registros do BD
    return render(request, 'galeria/index.html', {'cards': fotografias} )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    # buscar todos os ítens do nosso banco de dados
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True) # Busca todos os registros do BD    
    
    # Conferir se existe "Buscar" nas informações passadas peloa URL
    print(request.GET)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar'] # O que consta no input 
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) # Vai buscar na coluna nome se contém a palavra chave
    return render(request, "galeria/buscar.html", {"cards": fotografias})
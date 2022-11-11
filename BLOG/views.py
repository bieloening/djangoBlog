from django.shortcuts import render
from .models import Publicacoes

def inicio(request):
    publicacoes = Publicacoes.objects.all()
    return render(request, 'inicio.html', {'publicacoes':publicacoes})

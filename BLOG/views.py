from django.shortcuts import redirect, render
from .models import Publicacoes
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='logar')
def inicio(request):
    publicacoes = Publicacoes.objects.all()
    return render(request, 'inicio.html', {'publicacoes':publicacoes})

def postar(request):
    publicacoes = Publicacoes.objects.all()
    return render(request, 'postar.html', {'publicacoes':publicacoes})


def adicionar_informacao(request):


    titulo_post = request.POST.get('titulo_post')
    descricao_post = request.POST.get('descricao_post')
    imagem_post = request.POST.get('imagem_post')
    data_post = request.POST.get('data_post')


    Publicacoes.objects.create(titulo=titulo_post, descricao=descricao_post, imagem=imagem_post, criado_em=data_post, autor=request.user.id)

    return redirect('home')


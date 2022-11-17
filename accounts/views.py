from django.shortcuts import render, redirect
from django.contrib import auth

def user_login(request):

    if request.method == 'POST':
        usuario = request.POST.get('logarUsuario')
        senha = request.POST.get('logarSenha')

        check = auth.authenticate(request, username=usuario, password=senha)

        if check is not None:
            auth.login(request, check)
            return redirect('home')
        else:
            return redirect('login')

    else:
        return render(request, 'logar.html')
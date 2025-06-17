from django.shortcuts import render, redirect
from .models import Usuarios

def home(request):
    return render(request, 'todos/index.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('email')
        email = request.POST.get('password')
        if nome and email:
            novoUsuario = Usuarios(nome=nome, email=email)
            novoUsuario.save()
            return redirect('usuarios')  # Redireciona para evitar reenvio do formulário

    contexto = {
        'usuarios': Usuarios.objects.all()
    }
    return render(request, 'todos/usuarios.html', contexto)
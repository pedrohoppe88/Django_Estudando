from django.shortcuts import render
from .models import Todo
from .models import Usuarios

def home(request):
    Todos = Todo.objects.all()  # Obtém todas as tarefas do banco de dados
    return render(request, 'todos/index.html', {"todos": Todos})  # Renderiza o template com as tarefas

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novoUsuario = Usuarios()
    request.method = 'POST'
    novoUsuario = request.POST.get('email')
    novoUsuario = request.POST.get('password')
    
    # exibir os user já cadastrados em uma tela
    
    usuarios = {
        'usuarios': Usuarios.objects.all()  # Obtém todos os usuários do banco de dados 
        
    }
    #retornar os dados para a página HTML
    return render(request, 'todos/usuarios.html', usuarios)
    
    
    #nome = request.POST.get('email')
    #email = request.POST.get('password')
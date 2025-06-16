from django.shortcuts import render
from .models import Todo

def home(request):
    Todos = Todo.objects.all()  # Obtém todas as tarefas do banco de dados
    return render(request, 'todos/index.html', {"todos": Todos})  # Renderiza o template com as tarefas
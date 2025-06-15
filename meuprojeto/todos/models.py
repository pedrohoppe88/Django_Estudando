from django.db import models

class Todo(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)  # Título da tarefa
    concluido = models.BooleanField(default=False)  # Se está concluída ou não
    criado_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    deadline = models.DateTimeField(null=True, blank=True)  # Data limite para conclusão
    finished = models.DateTimeField(null=True, blank=True)  # Data de conclusão

    def __str__(self):
        return self.titulo
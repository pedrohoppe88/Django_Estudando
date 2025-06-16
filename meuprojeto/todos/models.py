from django.db import models

class Users(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Todo(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    concluido = models.BooleanField(default=False)
    criado_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    finished = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.titulo
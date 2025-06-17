from django.contrib import admin
from django.urls import path
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # rota para a página inicial
    #path('usuarios/', views.usuarios, name='usuarios'),
]
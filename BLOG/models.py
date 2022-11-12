from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Publicacoes(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField()
    descricao = models.TextField(max_length=255)
    criado_em = models.DateField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural='Publicações'


    
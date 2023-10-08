from django.db import models

class Disco(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    selo_fonografico = models.CharField(max_length=255)
    ano = models.IntegerField()
    pais = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome



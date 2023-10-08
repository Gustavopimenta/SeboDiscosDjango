from django.db import models

class SeloFonografico(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class Artista(models.Model):
    nome = models.CharField(max_length=255)
    discos = models.ManyToManyField('Disco', related_name='artistas')
    
    def __str__(self):
        return self.nome

class Disco(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    selo_fonografico = models.ForeignKey(SeloFonografico, on_delete=models.CASCADE)
    ano = models.IntegerField()
    pais = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.nome

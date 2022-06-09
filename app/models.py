from django.db import models
from datetime import date

# Create your models here.
class Vagas(models.Model):
    vaga = models.CharField(max_length=150)
    description = models.CharField(max_length=8000)
    data = models.DateField("%d/%m/%Y")

class Candidatos(models.Model):
    nome = models.CharField(max_length=150)
    vaga = models.CharField(max_length=150)
    pretensao = models.FloatField()
    area = models.CharField(max_length=150)
    previsao = models.DateField("%d/%m/%Y")
    indicacao = models.CharField(max_length=150)
    indicador = models.CharField(max_length=150)

# from djmoney.models.fields import MoneyField
from django.db import models
from datetime import datetime,date
from django.db.models import deletion

# Create your models here.
class Vagas(models.Model):
    vaga = models.CharField(max_length=150)
    area = models.CharField(null=True, blank=True, max_length=150)
    description = models.CharField(max_length=8000)
    data = models.DateField("%d/%m/%Y", auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return  self.vaga
        return self.area

class Candidatos(models.Model):
    nome = models.CharField(max_length=150)
    vaga = models.ForeignKey(Vagas, null=False, related_name='candidato_vaga', on_delete=deletion.CASCADE)
    pretensao = models.DecimalField (max_digits = 9, decimal_places = 2, null=True)
    previsao = models.DateField(null=True)
    indicacao = models.CharField(max_length=150)
    indicador = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
    
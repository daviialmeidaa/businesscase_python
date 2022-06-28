# from djmoney.models.fields import MoneyField
from django.db import models
from datetime import datetime,date
from django.db.models import deletion

# Create your models here.

class Areas(models.Model):
    area = models.CharField(max_length=150)

    def __str__(self):
        return self.area

class IndicacaoModel(models.Model):
    indicacao_poll = models.CharField(max_length=150)

    def __str__(self):
        return self.indicacao_poll        

class Parceiros(models.Model):
    parceiro = models.CharField(max_length=150)     

    def __str__(self):
        return self.parceiro          


class Vagas(models.Model):
    vaga = models.CharField(max_length=150)
    area = models.ForeignKey(Areas, null=True, blank=True, related_name='areas_vagas', on_delete=deletion.DO_NOTHING)
    description = models.CharField(max_length=8000)
    data = models.DateField("%d/%m/%Y", auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return  self.vaga
        return self.area


class Candidatos(models.Model):
    nome = models.CharField(max_length=150)
    vaga = models.ForeignKey(Vagas, null=False, related_name='candidato_vagas', on_delete=deletion.CASCADE)
    email = models.EmailField(null=True, blank=True, max_length=150)
    pretensao = models.DecimalField (max_digits = 9, decimal_places = 2, null=True, blank=True)
    previsao = models.DateField(null=True)
    indicacao = models.ForeignKey(IndicacaoModel, null=True, blank=True, related_name='indicacao', on_delete=deletion.DO_NOTHING)
    indicador = models.ForeignKey(Parceiros, null=True, blank=True, related_name='indicacao', on_delete=deletion.DO_NOTHING)

    def __str__(self):
        return self.nome
        return self.vaga

 
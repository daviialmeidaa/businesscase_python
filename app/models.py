# from djmoney.models.fields import MoneyField
from django.db import models
from django.db.models import deletion
from datetime import datetime, date
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

class Modalidades(models.Model):
    modalidade_contratacao = models.CharField(max_length=150)        

    def __str__(self):
        return self.modalidade_contratacao


class Colaboradores(models.Model):
    nome = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    area = models.ForeignKey(Areas, null=True, blank=True, related_name='indicacao', on_delete=deletion.DO_NOTHING)
    modalidade_contratacao = models.ForeignKey(Modalidades, null=True, blank=True, related_name='modalidade', on_delete=deletion.DO_NOTHING)
    data_inicio = models.DateTimeField('Event Date', null=True)
    periodo = models.IntegerField(null=True)
    tipo_ferias = models.CharField(max_length=150, null=True)
    proximas_ferias = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.nome

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.data_inicio.date() -today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped


class regras_ferias(models.Model):
    modalidade_contratacao = models.ForeignKey(Modalidades, null=True, blank=True, related_name='modalidade_colaborador', on_delete=deletion.CASCADE)
    minimo_dias = models.DurationField(null=True, blank=True)
    tempo_max = models.DurationField(null=True, blank=True)
    periodo = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.modalidade_contratacao

class TiposFerias(models.Model):
    tipo_ferias = models.CharField(max_length=150)

    def __str__(self):
        return self.tipo_ferias        

class DefinirFerias(models.Model):
    tipo_ferias = models.ForeignKey(TiposFerias, null=True, blank=True, related_name='tipos_ferias', on_delete=deletion.CASCADE)
    data_saida = models.DateField("%d/%m/%Y", auto_now_add=False, auto_now=False, blank=True)
    data_retorno = models.DateField("%d/%m/%Y", auto_now_add=False, auto_now=False, blank=True)
    
    def __str__(self):
        return self.tipo_ferias

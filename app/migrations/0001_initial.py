# Generated by Django 4.0.5 on 2022-06-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('vaga', models.CharField(max_length=150)),
                ('pretensao', models.FloatField()),
                ('area', models.CharField(max_length=150)),
                ('previsao', models.DateField(verbose_name='%d/%m/%Y')),
                ('indicacao', models.CharField(max_length=150)),
                ('indicador', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaga', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=8000)),
                ('data', models.DateField(verbose_name='%d/%m/%Y')),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-11 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_modalidades_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regras_ferias',
            name='modalidade_contratacao',
        ),
        migrations.AddField(
            model_name='regras_ferias',
            name='modalidade_contratada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modalidade_colaborador', to='app.colaboradores'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='modalidade_contratacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modalidade', to='app.modalidades'),
        ),
    ]
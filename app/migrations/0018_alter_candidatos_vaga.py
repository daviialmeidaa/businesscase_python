# Generated by Django 4.0.5 on 2022-06-27 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_candidatos_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='vaga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidato_vagas', to='app.vagas'),
        ),
    ]

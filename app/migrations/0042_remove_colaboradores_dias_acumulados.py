# Generated by Django 4.0.5 on 2022-07-11 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_alter_colaboradores_data_inicio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaboradores',
            name='dias_acumulados',
        ),
    ]

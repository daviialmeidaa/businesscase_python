# Generated by Django 4.0.5 on 2022-06-27 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_candidatos_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatos',
            name='vaga',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_candidatos_pretensao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatos',
            name='area',
        ),
        migrations.AddField(
            model_name='vagas',
            name='area',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
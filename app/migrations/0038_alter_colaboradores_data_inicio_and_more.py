# Generated by Django 4.0.5 on 2022-07-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_colaboradores_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='data_inicio',
            field=models.DateTimeField(verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='dias_acumulados',
            field=models.CharField(max_length=150),
        ),
    ]
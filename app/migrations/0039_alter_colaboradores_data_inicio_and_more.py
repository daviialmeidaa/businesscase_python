# Generated by Django 4.0.5 on 2022-07-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_colaboradores_data_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='data_inicio',
            field=models.DateField(blank=True, verbose_name='%d/%m/%Y'),
        ),
        migrations.AlterField(
            model_name='colaboradores',
            name='dias_acumulados',
            field=models.DateTimeField(verbose_name='Event Date'),
        ),
    ]
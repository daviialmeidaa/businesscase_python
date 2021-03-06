# Generated by Django 4.0.5 on 2022-06-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_candidatos_pretensao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='pretensao',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='vagas',
            name='data',
            field=models.DateField(blank=True, verbose_name='%d/%m/%Y'),
        ),
    ]

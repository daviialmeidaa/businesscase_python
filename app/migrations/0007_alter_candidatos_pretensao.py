# Generated by Django 4.0.5 on 2022-06-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_candidatos_pretensao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='pretensao',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='R$'),
        ),
    ]

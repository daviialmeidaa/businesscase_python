# Generated by Django 4.0.5 on 2022-06-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_candidatos_pretensao_alter_vagas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='pretensao',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]

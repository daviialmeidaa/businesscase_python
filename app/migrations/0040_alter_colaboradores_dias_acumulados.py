# Generated by Django 4.0.5 on 2022-07-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_colaboradores_data_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='dias_acumulados',
            field=models.DateTimeField(null=True, verbose_name='Event Date'),
        ),
    ]
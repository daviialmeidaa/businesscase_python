# Generated by Django 4.0.5 on 2022-06-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_parceiros_alter_candidatos_indicador'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatos',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-27 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_candidatos_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatos',
            name='area',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-28 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_vagas_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicacaoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicacao_poll', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='candidatos',
            name='indicacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='indicacao', to='app.indicacaomodel'),
        ),
    ]

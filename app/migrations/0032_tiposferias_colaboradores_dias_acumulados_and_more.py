# Generated by Django 4.0.5 on 2022-07-11 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_definirferias'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposFerias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_ferias', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='dias_acumulados',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='periodo',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='proximas_ferias',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='colaboradores',
            name='tipo_ferias',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='definirferias',
            name='data_retorno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='definirferias',
            name='data_saida',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='definirferias',
            name='tipo_ferias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tipos_ferias', to='app.tiposferias'),
        ),
    ]

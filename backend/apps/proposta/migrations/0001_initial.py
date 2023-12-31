# Generated by Django 4.2.2 on 2023-06-16 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_campo', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Campo',
                'verbose_name_plural': 'Campos',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Formulario',
                'verbose_name_plural': 'Formularios',
            },
        ),
        migrations.CreateModel(
            name='PropostaRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocolo', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('aprovado', 'Aprovado'), ('negado', 'Negado')], max_length=10)),
            ],
            options={
                'verbose_name': 'Proposta',
                'verbose_name_plural': 'Propostas',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=500)),
                ('protocolo', models.CharField(max_length=100)),
                ('id_campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposta.campo')),
                ('id_formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposta.formulario')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.AddField(
            model_name='campo',
            name='id_formulario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposta.formulario'),
        ),
    ]

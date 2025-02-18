# Generated by Django 5.1.6 on 2025-02-18 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('matricula', models.IntegerField()),
                ('curso', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=70)),
                ('autor', models.CharField(max_length=70)),
                ('ano_publicacao', models.IntegerField()),
                ('editora', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biblioteca.aluno')),
                ('id_livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='biblioteca.livro')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('slug', models.SlugField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Catalogo_Preguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('bloque', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('website_corporativo', models.URLField(max_length=1000)),
                ('website_integridad', models.URLField(max_length=1000)),
                ('cuestionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mxvscorrupcion.Cuestionario')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
                'ordering': ['pais'],
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField(null=True)),
                ('reactivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxvscorrupcion.Catalogo_Preguntas')),
            ],
        ),
        migrations.CreateModel(
            name='Sectores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxvscorrupcion.Paises'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mxvscorrupcion.Sectores'),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='preguntas',
            field=models.ManyToManyField(to='mxvscorrupcion.Pregunta'),
        ),
    ]

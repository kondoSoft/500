# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-18 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Sectores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
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
    ]

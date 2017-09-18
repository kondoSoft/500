# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-18 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='paises',
            options={'ordering': ['pais'], 'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelOptions(
            name='sectores',
            options={'ordering': ['nombre'], 'verbose_name': 'Sector', 'verbose_name_plural': 'Sectores'},
        ),
    ]

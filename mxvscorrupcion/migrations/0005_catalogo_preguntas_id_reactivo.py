# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-26 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0004_auto_20171025_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo_preguntas',
            name='id_reactivo',
            field=models.CharField(default='xx', max_length=200),
            preserve_default=False,
        ),
    ]

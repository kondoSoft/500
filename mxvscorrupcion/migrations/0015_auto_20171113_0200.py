# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-13 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0014_auto_20171112_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestionario',
            name='Corte',
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

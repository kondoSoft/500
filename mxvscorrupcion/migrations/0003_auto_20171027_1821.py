# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-27 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0002_auto_20171027_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuestas',
            name='opcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='valor',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-26 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0003_auto_20170926_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='respuesta',
            field=models.TextField(null=True),
        ),
    ]

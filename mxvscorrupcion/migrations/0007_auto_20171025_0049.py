# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0006_auto_20171025_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-10 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0004_auto_20171109_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]

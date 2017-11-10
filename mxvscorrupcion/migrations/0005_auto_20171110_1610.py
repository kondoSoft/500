# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-10 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mxvscorrupcion', '0004_auto_20171109_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='id',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='perfil', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

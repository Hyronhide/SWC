# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0003_auto_20161102_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='tipo_programa',
            field=models.ManyToManyField(blank=True, null=True, to='programas.Tipo_Programa'),
        ),
    ]

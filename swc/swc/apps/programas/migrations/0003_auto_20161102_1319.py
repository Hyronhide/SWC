# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0002_responsable_numero_identificador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='ocupacion',
            name='nombre',
            field=models.CharField(max_length=120),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsable',
            name='numero_identificador',
            field=models.CharField(default=12, max_length=11),
            preserve_default=False,
        ),
    ]

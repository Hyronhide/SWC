# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 17:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Centro_Formacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=11)),
                ('fase', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
                ('tipo_identificacion', models.CharField(choices=[('nit', 'NIT'), ('its', 'ITS'), ('cc', 'CC')], max_length=3)),
                ('numero_identificacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=11)),
                ('identificador_unico', models.CharField(max_length=11)),
                ('estado', models.CharField(choices=[('en_ejecucion', 'En ejecucion'), ('terminada', 'Terminada'), ('terminada_por_fecha', 'Terminada por fecha')], max_length=20)),
                ('jornada', models.CharField(choices=[('diurna', 'Diurna'), ('mixta', 'Mixta')], max_length=10)),
                ('tipo_formacion', models.CharField(choices=[('a_la_medida', 'A la medida'), ('no_a_la_medida', 'No a la medida')], max_length=20)),
                ('fecha_inicio', models.DateField(max_length=50)),
                ('fecha_terminacion', models.DateField(max_length=50)),
                ('etapa', models.CharField(choices=[('lectiva', 'Lectiva'), ('practica', 'Practica')], max_length=20)),
                ('modalidad', models.CharField(choices=[('presencial', 'Presencial'), ('virtual', 'Virtual')], max_length=20)),
                ('ampliacion_cobertura', models.CharField(max_length=1)),
                ('numero_cursos', models.IntegerField()),
                ('total_aprendices_masculinos', models.IntegerField()),
                ('total_aprendices_femeninos', models.IntegerField()),
                ('toal_aprendices', models.IntegerField()),
                ('horas_contratistas', models.TimeField()),
                ('horas_contratistas_externos', models.TimeField()),
                ('horas_monitores', models.TimeField()),
                ('horas_inst_empresa', models.TimeField()),
                ('total_horas', models.TimeField()),
                ('total_aprendices_activos', models.IntegerField()),
                ('programa_especial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_Formacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('codigo', models.CharField(max_length=11)),
                ('version', models.CharField(max_length=11)),
                ('duracion', models.IntegerField()),
                ('tipo', models.CharField(choices=[('regular', 'Regular'), ('especial', 'Especial')], max_length=10)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Area')),
                ('centro_formacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Centro_Formacion')),
                ('nivel_de_formacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Nivel_Formacion')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado_Aprendizaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Sector_Nuevo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='programa',
            name='nuevo_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Sector_Nuevo'),
        ),
        migrations.AddField(
            model_name='programa',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Ocupacion'),
        ),
        migrations.AddField(
            model_name='programa',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Sector'),
        ),
        migrations.AddField(
            model_name='programa',
            name='tipo_programa',
            field=models.ManyToManyField(to='programas.Tipo_Programa'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Programa'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Responsable'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Pais'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Empresa'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Programa'),
        ),
        migrations.AddField(
            model_name='competencia',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Programa'),
        ),
        migrations.AddField(
            model_name='centro_formacion',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programas.Municipio'),
        ),
    ]

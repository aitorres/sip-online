# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-06 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20181105_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='dpto',
            new_name='departamento',
        ),
        migrations.AlterField(
            model_name='departamento',
            name='jefe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jefe_de', to='gestion.Profesor'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='cedula',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='asignaturas',
            field=models.ManyToManyField(to='gestion.Asignatura'),
        ),
    ]

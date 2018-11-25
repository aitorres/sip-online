# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20181106_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='asignaturas',
            field=models.ManyToManyField(blank=True, to='gestion.Asignatura'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='disponibilidad',
            field=models.ManyToManyField(blank=True, to='gestion.Disponibilidad'),
        ),
    ]

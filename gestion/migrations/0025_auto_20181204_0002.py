# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0024_asignacionprofesoral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertatrimestral',
            name='denominacion',
            field=models.CharField(max_length=50),
        ),
    ]

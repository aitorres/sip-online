# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-06 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0027_auto_20181205_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='ofertatrimestral',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion.Departamento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ofertatrimestral',
            name='trimestre',
            field=models.CharField(max_length=4),
        ),
    ]

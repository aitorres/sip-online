# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0022_merge_20181125_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfertaTrimestral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.CharField(max_length=4)),
                ('codigo', models.CharField(max_length=7, unique=True)),
                ('unidad_creditos', models.IntegerField(default=0)),
                ('denominacion', models.CharField(max_length=20)),
                ('profesor', models.ManyToManyField(blank=True, to='gestion.Profesor')),
            ],
        ),
    ]

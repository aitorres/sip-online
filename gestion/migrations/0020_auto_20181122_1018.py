# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-22 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0019_auto_20181122_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='requisitos',
            field=models.ManyToManyField(blank=True, null=True, to='gestion.Asignatura'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-20 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0031_auto_20181219_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinacion',
            name='codigo',
            field=models.CharField(default='', max_length=3, unique=True),
            preserve_default=False,
        ),
    ]

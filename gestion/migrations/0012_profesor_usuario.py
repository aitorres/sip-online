# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-25 20:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0011_auto_20181108_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='usuario',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

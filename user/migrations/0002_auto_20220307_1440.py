# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2022-03-07 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.DateField(default='1990-1-1', max_length=8, verbose_name='出⽣⽇    '),
        ),
    ]
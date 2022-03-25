# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2022-03-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.IntegerField()),
                ('uid2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Swiperd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='滑动者的ID')),
                ('sid', models.IntegerField(verbose_name='被滑动者的ID')),
                ('stype', models.CharField(choices=[('like', '喜欢'), ('superlike', '超级喜欢'), ('dislike', '不喜欢')], max_length=10, verbose_name='滑动的类型')),
                ('stime', models.DateTimeField(auto_now_add=True, verbose_name='滑动时间')),
            ],
        ),
    ]

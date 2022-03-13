# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2022-03-13 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220307_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_sex', models.CharField(choices=[('male', '男性'), ('female', '女性')], max_length=8, verbose_name='匹配的性别')),
                ('dating_location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('广州', '广州'), ('重庆', '重庆'), ('西安', '西安'), ('武汉', '武汉'), ('沈阳', '沈阳')], max_length=20, verbose_name='⽬标城市')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最⼩交友年龄')),
                ('max_dating_age', models.IntegerField(default=50, verbose_name='最⼤交友年龄')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最⼩查找范围')),
                ('max_distance', models.IntegerField(default=30, verbose_name='最⼤查找范围')),
                ('vibration', models.BooleanField(default=True, verbose_name='开启震动')),
                ('only_matche', models.BooleanField(default=True, verbose_name='只让匹配的⼈看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='⾃动播放视频')),
            ],
        ),
    ]

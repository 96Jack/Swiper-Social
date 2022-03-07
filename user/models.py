from random import choices
from telnetlib import SE
from django.db import models

# Create your models here.

class User(models.Model):
    # 提供可选项，元组，前面一个值存在数据库，后面的值时提示用
    SEX = (
        ('male',   '男性'),
        ('female', '女性')
    )
    LOCATION = (
        ('北京',('北京')),
        ('上海',('上海')),
        ('深圳',('深圳')),
        ('广州',('广州')),
        ('重庆',('重庆')),
        ('西安',('西安')),
        ('武汉',('武汉')),
        ('沈阳',('沈阳')),
    )
    phonenum      = models.CharField(max_length=15, unique=True, verbose_name="⼿机号     ")
    nickname      = models.CharField(max_length=20, verbose_name="昵称 ")
    sex           = models.CharField(max_length=8, choices=SEX, verbose_name="性别  ")
    # birth_year    = models.CharField( verbose_name="出⽣年")
    # birth_month   = models.CharField( verbose_name="出⽣⽉    ")
    birth_day     = models.CharField(max_length=8, default='1990-1-1', verbose_name="出⽣⽇    ")
    # 形象介绍的内容较多，一般存在服务器，给网址
    avatar        = models.CharField( max_length=256, verbose_name="个⼈形象   ")
    location      = models.CharField( max_length=20, choices=LOCATION, verbose_name="常居地         ")
             





# -*- encoding: utf-8 -*-
'''
file       :__init__.py
Description:
Date       :2022/03/17 16:10:17
Author     :Xu Zhiwen
version    :python3.7.8
'''


import os

from celery import Celery, platforms

from tasks import config


# root用户开启celery进程:If you really want to continue then you have to set the C_FORCE_ROOT environment variable
platforms.C_FORCE_ROOT = True

# 加载django环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
# 创建App
celery_app = Celery('app_name')
# 从对象（配置模块）中引入配置
celery_app.config_from_object(config)
# 自动查找django封装的任务
celery_app.autodiscover_tasks() 


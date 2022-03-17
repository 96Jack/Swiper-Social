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


# If you really want to continue then you have to set the C_FORCE_ROOT environment variable
platforms.C_FORCE_ROOT = True 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
celery_app = Celery('worker')
celery_app.config_from_object(config)
# 自动查找django封装的任务
celery_app.autodiscover_tasks()

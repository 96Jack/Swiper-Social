# -*- encoding: utf-8 -*-
'''
file       :task.py
Description: for celery practice
Date       :2022/03/16 22:27:51
Author     :Xu Zhiwen
version    :python3.7.8
'''



import time
from celery import Celery

# 0号数据库
broker = 'redis://127.0.0.1:6379/0'
backend = 'redis://127.0.0.1:6379/0'
app  = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    time.sleep(1)
    return x + y


# =====================================================================
# celery端
# Task task.add[ce86df13-7bbf-4f70-82b4-9a08a609693e] received
#： 接收ipython端发送的异步任务 ： [任务编号]

# =====================================================================
#ipython 端
# n = add.delay(20, 30)
# n.result : 查看结果
# n
#<AsyncResult: 2400e753-831f-4566-8042-2cbeddcf40ab>


# ======================================================================
# redis端
# from redis import Redis
# r = Redis()
# r.keys()
# 》：
# [b'celery-task-meta-e823ff88-0eac-46b7-8588-509d7bfe367b',
#  b'celery-task-meta-2400e753-831f-4566-8042-2cbeddcf40ab',
#  b'celery-task-meta-ce86df13-7bbf-4f70-82b4-9a08a609693e',
#  b'_kombu.binding.celery',
#  b'_kombu.binding.celery.pidbox',
#  b'_kombu.binding.celeryev']

#  r.get('celery-task-meta-e823ff88-0eac-46b7-8588-509d7bfe367b')
# celery执行的结果以字符串的形式保存在redis的key中：结果为json字符串
# Out[20]: b'{"status": "SUCCESS", "result": 50, "traceback": null, "children": [], "date_done": "2022-03-16T14:26:31.131207", "task_id": "e823ff88-0eac-46b7-8588-509d7bfe367b"}'

from statistics import mode
from django.db.models import query
from django.db import models

from libs.cache import  rds
from common.keys import MODEL_KEY

def get(self, *args, **kwargs):
    """带缓处理的objects.get() 方法 : 使用MonkeyPatch统一增加缓存层(8-9)"""
    # 从缓存获取数据
    pk = kwargs.get('pk') or kwargs.get('id')
    if pk is not None:
        key = MODEL_KEY % (self.model.__name__, pk)
        model_obj = rds.get(key)
        if isinstance(model_obj, self.model):
            # print("从缓存中获取model: %s" % model_obj)
            return model_obj

    # 缓存中没有，从数据库中获取
    model_obj = self._get(*args, **kwargs)
    # print("从数据库中获取model: %s" % model_obj)

    # 将取出的数据写入缓存
    key =MODEL_KEY % (self.model.__name__, model_obj.pk)
    rds.set(key, model_obj)
    # print("将model写入缓存: %s" % model_obj)
    return model_obj
    
def save(self, force_insert=True, force_update=False, using=None, update_fields=None):
    #使用原来的save() 将model写入数据库
    self._save(force_insert, force_update, using, update_fields)
    #将model_obj保存到缓存
    key = MODEL_KEY % (self.__class__.__name__, self.pk)
    rds.set(key, self)
    
def patch():
    """通过MonkeyPatch给原ORM添加缓存处理"""
    # 保留原get方法
    query.QuerySet._get = query.QuerySet.get    
    # 重写get方法
    query.QuerySet.get  = get

    models.Model._save = models.Model.save
    # 重写save方法
    models.Model.save = save


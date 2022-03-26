from django.db import models

# Create your models here.

class Vip(models.Model):
    """会员表"""
    name = models.CharField(max_length=10, unique=True, verbose_name='会员名称')
    level = models.IntegerField(default=0, verbose_name='会员名称')
    price = models.FloatField(default=0.0, verbose_name='当前会员对应的价格')
    days = models.IntegerField(default=0, verbose_name='购买的天数')

class Permission(models.Model):
    """权限表"""
    name = models.CharField(max_length=10, unique=True, verbose_name='权限名称')

class VipPermRelation(models.Model):
    """会员和权限的关系表 : 多对多
    关系：
        一级会员  超级喜欢
        二级会员  超级喜欢
        二级会员  反悔三次
        三级会员  超级喜欢
        三级会员  反悔三次
        三级会员  查看喜欢过我的人
    """
    vip_id = models.IntegerField(verbose_name='会员的ID')
    perm_id = models.IntegerField(verbose_name='权限的ID')

    


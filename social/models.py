from django.db import models
from django.db.models import Q
# Create your models here.

class Swiperd(models.Model):
    '''滑动记录'''
    STYPE = (
        ('like', '喜欢'),
        ('superlike', '超级喜欢'),
        ('dislike', '不喜欢'),
    )
    uid = models.IntegerField(verbose_name='滑动者的ID')
    sid = models.IntegerField(verbose_name='被滑动者的ID')
    stype = models.CharField(max_length=10, choices=STYPE,verbose_name='滑动的类型')
    stime = models.DateTimeField(auto_now_add=True, verbose_name='滑动时间')

    @classmethod
    def is_liked(cls, uid, sid):
        """检查是否喜欢过某人"""
        # condition = Q(stype='like') | Q(stype='superlike')
        # cls.objecccgts.filter(uid=uid, sid=sid, stype=condition)
        return  cls.objects.filter(uid=uid, sid=sid, stype__in=['like', 'superlike']).exists()

    @classmethod
    def swipe(cls, uid, sid, stype):
        if stype not in ['like','superlike','dislike']:
            return # TODO 返回状态码
        
        if cls.objects.filter(uid=uid, sid=sid, stype=stype):
            return # TODO 重复滑动状态码     
        return cls.objects.create(uid=uid, sid=sid, stype=stype)

class Friend(models.Model):
    '''友好关系'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friends(cls, uid, sid):
        """创建友好关系"""
        uid1, uid2 = (sid, uid) if uid > sid else (uid, sid)
        # get_or_create(): 先查询再创建：避免重复创建同一个人
        cls.objects.get_or_create(uid1=uid1, uid2=uid2)

from common import stat
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
        """执行第一次滑动"""
        # 检查 stype是否正确
        if stype not in ['like','superlike','dislike']:
            # 返回滑动类型错误
            raise stat.SwiperTypeError

        # 检查是否滑动过当前用户
        if cls.objects.filter(uid=uid, sid=sid, stype=stype):
            raise stat.SwiperRepeatError #  重复滑动状态码     

        return cls.objects.create(uid=uid, sid=sid, stype=stype)

    @classmethod
    def who_liked_me(cls, uid):
        """查看谁喜欢过我"""
        return cls.objects.filter(sid=uid, stype__in=['like', 'superlike'])\
                          .values_list('uid', flat=True) # 只取出querryset元组中的一个元素

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

    @classmethod
    def friend_ids(cls, uid):
        """查询自己的所有好友ID"""
        condition = Q(uid1=uid) | Q(uid2=uid)
        friend_relations = cls.objects.filter(condition)
        uid_list = []
        for relation in friend_relations:
            friend_id = relation.uid2 if relation.uid1 == uid else relation.uid1
            uid_list.append(friend_id)
        return uid_list

    @classmethod
    def break_off(cls, uid, sid):
        """断绝好友关系"""
        uid1, uid2 = (sid, uid) if uid > sid else (uid, sid)
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()



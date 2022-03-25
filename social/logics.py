import time 
import datetime

from common.keys import SUPERLIKED_KEY
from libs.cache import rds
from user.models import User
from social.models import Friend, Swiperd

def rcmd(user):
    '''推荐可滑动的用户'''
    profile = user.profile
    today = datetime.date.today()

    # 最早出生的日期
    earliest_birthday = today -datetime.timedelta(profile.max_dating_age * 365)
    # 最晚出生日期
    latest_birthday = today - datetime.timedelta(profile.min_dating_age * 365)
    print("earliest_birthday:{}\n latest_birthday:{}".format(earliest_birthday,latest_birthday))

    # 取出滑过的用户; flat=True将元组转化成列表
    sid_list = Swiperd.objects.filter(uid=user.id).values_list('sid', flat=True)

    # VIP用户取出超级喜欢过自己，但是还没有被自己滑动过的用户ID： 使用ORM取出
    # -----------------------直接从数据库中取出：性能太差-------------------------
    # who_superlike_me = Swiperd.objects.filter(sid=user.id, stype='superlike')\
    #                                   .exclude(uid__in=sid_list)\
    #                                   .values_list('uid', flat=True)
    # --------------------------------------------------------------------------

    # 使用Redis取出
    superliked_me_id_list = [int(uid) for uid in rds.zrange(SUPERLIKED_KEY % user.id , 0, 19)]
    superliked_me_users = User.objects.filter(id__in=superliked_me_id_list)

    # 筛选出匹配的用户; 排除已经滑过的用户
    other_count = 20 - len(superliked_me_users)
    if other_count > 0:
        other_users = User.objects.filter(
            sex=profile.dating_sex,
            location=profile.dating_location,
            birth_day__gte=earliest_birthday,
            birth_day__lte=latest_birthday,
        ).exclude(id__in=sid_list)[:other_count]             # 懒加载
        users = superliked_me_users | other_users
    else:
        users = superliked_me_users
    return users

def like_someone(user, sid):
    '''喜欢某人'''
    # 避免重复插入同一个用户

    Swiperd.swipe(user.id, sid, 'like') # 添加滑动记录

    # 检查对方是否喜欢自己p
    if Swiperd.is_liked(sid, user.id):
        # 如果对方喜欢过自己，匹配成好友：外部通过类名调用类方法
        Friend.make_friends(user.id, sid)
        # 如果对方超级喜欢过你，将对方从你的超级喜欢列表中删除
        rds.zrem(SUPERLIKED_KEY % user.id, sid )
        return True
    else:
        return False
        

def superlike_someone(user, sid):
    """超级喜欢某人
    自己超级喜欢对方则一定会出现在对方的推荐列表里
    """
    Swiperd.swipe(user.id, sid, 'superlike') # 添加滑动记录
    rds.zadd(SUPERLIKED_KEY % sid , {user.id: time.time()})  # 将自己的id写入对方的优先推荐队列
    # 检查对方是否喜欢自己
    if Swiperd.is_liked(sid, user.id):
        # 如果对方喜欢过自己，匹配成好友：外部通过类名调用类方法
        Friend.make_friends(user.id, sid)
        # 如果对方超级喜欢过你，将对方从你的超级喜欢列表中删除
        rds.zrem(SUPERLIKED_KEY % user.id, sid )

        return True
    else:
        return False
    
def dislike_someone(user, sid):
    """不喜欢某人"""
    Swiperd.swipe(user.id, sid, 'superlike') # 添加滑动记录
     # 如果对方超级喜欢过你，将对方从你的超级喜欢列表中删除（推荐列表）
    rds.zrem(SUPERLIKED_KEY % user.id, sid )
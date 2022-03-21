import datetime
from statistics import mode
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

    # 筛选出匹配的用户; 排除已经滑过的用户
    users = User.objects.filter(
        sex=profile.dating_sex,
        location=profile.dating_location,
        birth_day__gte=earliest_birthday,
        birth_day__lte=latest_birthday,
    ).exclude(id__in=sid_list)[:20]             # 懒加载

    return userskmhb

def like_someone(user, sid):
    '''喜欢某人'''
    # 避免重复插入同一个用户

    Swiperd.swipe(user.id, sid, 'like') # 添加滑动记录

    # 检查对方是否喜欢自己p
    if Swiperd.is_liked(sid, user.id):
        # 如果对方喜欢过自己，匹配成好友：外部通过类名调用类方法
        Friend.make_friends(user.id, sid)
        return True
    else:
        return False
        

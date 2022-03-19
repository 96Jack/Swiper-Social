import datetime
from user.models import User

def rcmd(user):
    '''推荐可滑动的用户'''
    profile = user.profile
    today = datetime.date.today()

    # 最早出生的日期
    earliest_birthday = today -datetime.timedelta(profile.max_dating_age * 365)
    # 最晚出生日期
    latest_birthday = today - datetime.timedelta(profile.min_dating_age * 365)
    print("earliest_birthday:{}\n latest_birthday:{}".format(earliest_birthday,latest_birthday))
    # 筛选出匹配的用户
    users = User.objects.filter(
        sex=profile.dating_sex,
        location=profile.dating_location,

        birth_day__gte=earliest_birthday,
        birth_day__lte=latest_birthday,
    )[:20] # 懒加载

    # TODO: 删除划过的用户
    return users

    
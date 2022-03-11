

from cgitb import reset
from urllib import response
from django.core.cache import cache
import requests
import random
from common import keys
from swiper import cfg


def gen_randcode(length: int) -> str:
    """产生出指定长度的随机码"""
    # 多个字符相加，每次相加都会调用内存，占用资源
    # ''.join(['a', 'b']) 函数只会调用一次内存将列表内的所有字符拼在一起 
    chars = [str(random.randint(0, 9)) for i in range(length)]
    return ''.join(chars)


def send_vcode(phone):
    """
    指定模板单发
    {
   "code":"0",
   "msg":"OK", 
   "count":"1",
   "create_date":"2017-08-28 19:08:28",
   "smsid":"f96f79240e372587e9284cd580d8f953",
   "mobile":"18011984299",
   "uid":"2d92c6132139467b989d087c84a365d8"
    }
    """
    vcode = gen_randcode(6)
    # 将验证码设置在缓存中，并设置过期时间180s
    cache.set(keys.VCODE_KEY % phone, vcode, 180)
    print("验证码: ", vcode)
    
    # 设计模式之原型模式：不修改公共配置信息
    sms_args = cfg.YZX_ARGS.copy()
    sms_args['param'] = vcode
    sms_args['mobile'] = phone
    response = requests.post(cfg.YZX_API, json=sms_args)
    
    print("status_code:",response.status_code)
    # 检查最终的返回值
    if response.status_code == 200:
        result = response.json()
        print("YZX_result_code",result['code'])
        if result['code'] == '000000':
            return True 
    return False


def get_access_token(code):
    """
    token返回的数据类型:
    {
       "access_token": "ACCESS_TOKEN",
       "expires_in": 1234,
       "remind_in":"798114",
       "uid":"12341234"
    }
    """
    args = cfg.WB_ACCESS_TOKEN_ARGS.copy()
    args['code'] = code
    response = requests.post(cfg.WB_ACCESS_TOKEN_API, data=args)
    print("response.status_code:",response.status_code)
     # 检查最终的返回值
    if response.status_code == 200:
        result = response.json()
        print("ACCESS_token_status_code:=====================",result)
        access_token = result['access_token']
        wb_uid = result['uid']
        return access_token, wb_uid
    return None, None
    
def get_user_info(access_token, wb_uid):
    args = cfg.WB_USER_SHOW_ARGS.copy()
    args['access_token'] = access_token
    args['uid'] = wb_uid
    print('args========>:',args)
    response = requests.get(cfg.WB_USER_SHOW_API,params=args)
    # 检查返回值
    if response.status_code == 200:
        result = response.json()
        print("get_user_info_result:=========>",result)
        user_info = {
            'phonenum':    'WB_%s' % wb_uid,
            'nickname':    result['screen_name'],
            'sex'     :    'female' if result['gender'] == 'f' else 'male',
            'avatar'  :    result['avatar_hd'],
            'location':    result['location'].split(' ')[0],
        }
        return user_info
    return None

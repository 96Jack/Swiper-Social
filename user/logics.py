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
    vcode = gen_randcode(6)
    # 将验证码设置在缓存中，并设置过期时间180s
    cache.set(keys.VCODE_KEY % phone, vcode, 180)
    print("验证码: ", vcode)
    
    # 设计模式之原型模式：不修改公共配置信息
    sms_args = cfg.YZX_ARGS.copy()
    sms_args['param'] = vcode
    sms_args['mobile'] = phone
    response = requests.post(cfg.YZX_API, json=sms_args)

    # 检查最终的返回值
    if response.status_code == 200:
        result = response.json()
        if result['code'] == '000000':
            return True 
    return False



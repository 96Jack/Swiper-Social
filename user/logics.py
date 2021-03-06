import logging

from cgitb import reset
from urllib import response
from django.core.cache import cache
from django.forms import FilePathField
import requests
import random
from common import keys
from swiper import cfg
from tasks import celery_app
from libs.qn_cloud import upload_to_qn

inf_log = logging.getLogger('inf')

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
    inf_log.info("验证码: %s "% vcode)
    print("验证码: ", vcode)
    print("cached_vcode:",cache.get(keys.VCODE_KEY % phone))
    
    # 设计模式之原型模式：不修改公共配置信息
    sms_args = cfg.YZX_ARGS.copy()
    sms_args['param'] = vcode
    sms_args['mobile'] = phone
    response = requests.post(cfg.YZX_API, json=sms_args)
    
    # print("status_code:",response.status_code)
    # 检查最终的返回值
    if response.status_code == 200:
        result = response.json()
        # print("YZX_result_code",result['code'])
        # 云资讯平台未认证
        if result['code'] == '105140':
        # if result['code'] == '000000':
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
        # print("ACCESS_token_status_code:=====================",result)
        access_token = result['access_token']
        wb_uid = result['uid']
        return access_token, wb_uid
    return None, None
    
def get_user_info(access_token, wb_uid):
    args = cfg.WB_USER_SHOW_ARGS.copy()
    args['access_token'] = access_token
    args['uid'] = wb_uid
    # print('args========>:',args)
    response = requests.get(cfg.WB_USER_SHOW_API,params=args)
    # 检查返回值
    if response.status_code == 200:
        result = response.json()
        # print("get_user_info_result:=========>",result)
        user_info = {
            'phonenum':    'WB_%s' % wb_uid,
            'nickname':    result['screen_name'],
            # 三元运算
            'sex'     :    'female' if result['gender'] == 'f' else 'male',
            'avatar'  :    result['avatar_hd'],
            'location':    result['location'].split(' ')[0],
        }
        return user_info
    return None

def save_upload_avatar(filepath,  upload_avatar):
    '''保存上传的头像'''

    # upload_avatar type:  <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    # dir(upload_avatar) :  查看一个对象内部的属性和方法 
    with open(filepath, 'wb') as fp:
        for chunk in upload_avatar.chunks():
            fp.write(chunk)
    return "save avatar in local"

@celery_app.task
def handle_avatar(filename, filepath): 
# def handle_avatar(filepath, avatar): 
    '''上传个人形象'''
    # save_upload_avatar(filepath, avatar)
    return 'local in filepath:{} file  filename:{} upload_to_niu'.format(filepath, filename)
    # # 将文件上传到七牛云
    # avatar_url = upload_to_qn(filename, filepath)

    # # 保存avatar_url
    # request.user.avatar = avatar_url
    # request.save()

    #删除临时文件
    # os.remove(filepath)  
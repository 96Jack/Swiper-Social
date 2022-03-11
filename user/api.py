from os import access
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.cache import cache

from common import keys
from user import logics
from common import stat
from user.models import User
from swiper import cfg






# Create your views here.

def get_vcode(request):
    '''获取短信验证码'''
    # 字典.get()取值，取不到不报错
    # request.GET
    # request.POST
    # request.COOKIES ： 由浏览器传送到服务器
    # request.session ： 服务器传送
    # request.FILED
    # 请求的源信息：header内：request.META['HTTP_USER_AGENT'] WSGI规定

    phonenum = request.GET.get('phonenum')

    # 发送验证码，并检查是否发送成功
    if logics.send_vcode(phonenum):
        return JsonResponse({'code':stat.OK, 'data':None})
    else:
        return JsonResponse({'code':stat.VCODE_ERR, 'data':None})
    
    
    

def check_vcode(request):
    """进行验证,并且登录验证"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cached_vcode = cache.get(keys.VCODE_KEY % phonenum)
    if  vcode and cached_vcode and vcode == cached_vcode:
        # 取出用户
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            # 如果用户不存在，直接创建用户
            user = User.objects.create(
                phonenum=phonenum,
                nickname=phonenum
            )
        request.session['uid'] = user.id
        # 传入的数据可以被JsonResponse序列化,code:状态码，data:返回的数据
        # 实例对象user
        return JsonResponse({'code': stat.OK, 'data': user.to_dict()})
    else:
        return JsonResponse({'code':stat.INVILD_VCODE, 'data':None})

def wb_auth(request):
    """用户授权页"""
    return redirect(cfg.WB_AUTH_URL)

def callback(request):
    """"微博回调接口"""
    code = request.GET.get('code')
    # 获取授权令牌
    print("access_code",code)
    access_token, wb_uid = logics.get_access_token(code)
    if not access_token:
        return JsonResponse({'code': stat.ACCESS_TOKEN_ERR , 'data':None })

    #获取用户信息
    user_info = logics.get_user_info(access_token, wb_uid)
    print("user_info:+++++++++",user_info)
    if not user_info:
        return JsonResponse({'code': stat.USER_INFO_ERR , 'data':None })

    # 执行登录或注册
    try:
        user = User.objects.get(phonenum=user_info['phonenum'])
    except User.DoesNotExist:
        user = User.objects.create(**user_info)
    request.session['uid'] = user.id
    return JsonResponse({'code': stat.OK, 'data': user.to_dict()})
    


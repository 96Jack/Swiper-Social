from socket import J1939_EE_INFO_NONE
from django.http import JsonResponse
from django.shortcuts import render
from user import logics


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
        return JsonResponse({'code':0, 'data':None})
    else:
        return JsonResponse({'code':1000, 'data':None})
    
    
    

def check_vcode(request):
    """进行验证,并且登录验证"""
    ...
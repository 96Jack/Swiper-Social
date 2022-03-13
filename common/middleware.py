# -*- encoding: utf-8 -*-
'''
file       :middleware.py
Description: 中间件： 任何请求进来都需要操作的接口： 获取当前用户(频繁操作的动作)
Date       :2022/03/13 14:01:35
Author     :Xu Zhiwen
version    :python3.7.8
'''


from urllib import request
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from common import stat
from user.models import User

class AuthorizeMiddleware(MiddlewareMixin):
    '''登录验证中间件'''
    def process_request(self, request):
        uid = request.session.get('uid')
        if not uid:
            return JsonResponse({'code': stat.LOGIN_REQUIRED, 'data': None})
        # 获取当前用户：将用户信息绑定到request上，api接口通过request获取用户信息
        request.user = User.objects.get(id=uid)

# -*- encoding: utf-8 -*-
'''
file       :middleware.py
Description: 中间件： 任何请求进来都需要操作的接口： 获取当前用户(频繁操作的动作)
Date       :2022/03/13 14:01:35
Author     :Xu Zhiwen
version    :python3.7.8
'''
import logging

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

from common import stat
from libs.http import render_json
from user.models import User

err_log = logging.getLogger('err')

class AuthorizeMiddleware(MiddlewareMixin):
    '''登录验证中间件'''
    """设置限制：白名单"""
    WHITE_LIST = [
        "/api/user/get_vcode",
        "/api/user/check_vcode",
        "/weibo/wb_auth", 
        "/weibo/callback",
    ]
    def process_request(self, request):
        if request.path in self.WHITE_LIST:
            return
        uid = request.session.get('uid')
        if not uid:
            return JsonResponse({'code': stat.LoginRequired, 'data': None})
        # 获取当前用户：将用户信息绑定到request上，api接口通过request获取用户信息
        request.user = User.objects.get(id=uid)

# class LogicErrMiddleware(MiddlewareMixin):
#     """逻辑异常处理中间件"""
#     def process_exception(self, request, exception):
#         if isinstance(exception, stat.LogicErr):
#             err_log.error('LogicError [%s] %s'% (exception.code, exception.data))
#             return render_json(data=exception.data, code=exception.code)
        
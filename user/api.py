from django.shortcuts import render

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
    # 发送验证码
    ...
    

def check_vcode(request):
    """进行验证,并且登录验证"""
    ...
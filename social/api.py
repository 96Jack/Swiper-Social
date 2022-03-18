from distutils.errors import LinkError
from winreg import DisableReflectionKey
from django.shortcuts import render

# Create your views here.
from libs.http import render_json

def get_rcm_users(request):
    '''获取推荐用户'''
    ...
    return render_json()
def like(request):
    '''右滑-喜欢'''
    ...
    return render_json()
def superlike(request):
    '''上滑-超级喜欢'''
    ...
    return render_json()
def dislike(request):
    '''左滑-不喜欢'''
    ...
    return render_json()
def rewind(request):
    '''反悔'''
    ...
    return render_json()
def who_like_me(request):
    '''查看谁喜欢过我'''
    ...
    return render_json()
def firend_list(request):
    '''朋友列表'''
    ...
    return render_json()

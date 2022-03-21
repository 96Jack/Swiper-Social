# Create your views here.

from libs.http import render_json
from social import logics



def get_rcm_users(request):
    '''获取推荐用户'''
    users = logics.rcmd(request.user)
    result = [user.to_dict() for user in users]
    return render_json(result)

def like(request):
    '''右滑-喜欢'''
    sid = int(request.POST.get('sid'))
    is_matched = logics.like_someone(request.user, sid)
    return render_json({'matched':is_matched})
    
    
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

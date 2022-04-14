# Create your views here.

from pydoc import render_doc
from unittest import result
from libs.http import render_json
from social import logics
from social.models import Swiperd
from social.models import Friend
from user.models import User
from vip.logics import need_permission
from social.logics import set_score



def get_rcm_users(request):
    '''获取推荐用户'''
    users = logics.rcmd(request.user)
    result = [user.to_dict('vip_id', 'vip_expired') for user in users]
    # print("result:{}".format(result))
    return render_json(result)


def like(request):
    '''右滑-喜欢'''
    sid = int(request.POST.get('sid'))
    is_matched = logics.like_someone(request.user, sid)
    set_score(sid, 'like')
    return render_json({'matched':is_matched})
    
@need_permission
def superlike(request):
    '''上滑-超级喜欢'''
    sid = int(request.POST.get('sid'))
    is_matched = logics.superlike_someone(request.user, sid)
    set_score(sid, 'superlike')
    return render_json({'matched':is_matched})
    

def dislike(request):
    '''左滑-不喜欢'''
    sid = int(request.POST.get('sid'))
    logics.dislike_someone(request.user, sid)
    set_score(sid, 'dislike')
    return render_json()

@need_permission
def rewind(request):
    '''反悔'''
    logics.rewind_swiped(request.user)
    return render_json()

@need_permission
def show_liked_me(request):
    '''查看谁喜欢过我'''
    user_id_list = Swiperd.who_liked_me(request.user.id)
    users = User.objects.filter(id__in=user_id_list)
    result = [user.to_dict('vip_id', 'vip_expired') for user in users]
    return render_json(result)

def firend_list(request):
    '''朋友列表'''
    friend_id_list = Friend.friend_ids(request.user.id)
    users = User.objects.filter(id__in=friend_id_list)
    result = [user.to_dict('vip_id', 'vip_expired') for user in users]

    return render_json(result)




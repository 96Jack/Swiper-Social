from django.http import JsonResponse
from django.shortcuts import  redirect
from django.core.cache import cache

from common import keys
from user import logics
from common import stat
from user.froms import ProfileForm, UserForm
from user.models import User
from swiper import cfg
from libs.http import render_json





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
        return render_json()
    else:
        return render_json(code=stat.VCODE_ERR)
    
    
    

def check_vcode(request):
    """进行验证,并且登录验证"""
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cached_vcode = cache.get(keys.VCODE_KEY % phonenum)
    # print("=====================\n vcode:{}\n, cache_vcode:{}\n".format(vcode, cached_vcode))
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
        # 传入的数据可以被render_json序列化,code:状态码，data:返回的数据
        # 实例对象user
        return render_json(code=stat.OK, data=user.to_dict())
    else:
        return render_json(code=stat.INVILD_VCODE)

def wb_auth(request):
    """用户授权页"""
    return redirect(cfg.WB_AUTH_URL)

def callback(request):
    """"微博回调接口"""
    code = request.GET.get('code')
    # 获取授权令牌
    # print("access_code",code)
    access_token, wb_uid = logics.get_access_token(code)
    if not access_token:
        return render_json(code=stat.ACCESS_TOKEN_ERR )

    #获取用户信息
    user_info = logics.get_user_info(access_token, wb_uid)
    print("user_info:+++++++++",user_info)
    if not user_info:
        return render_json(code=stat.USER_INFO_ERR)

    # 执行登录或注册
    try:
        user = User.objects.get(phonenum=user_info['phonenum'])
    except User.DoesNotExist:
        user = User.objects.create(**user_info)
    request.session['uid'] = user.id
    return render_json(code=stat.OK, data=user.to_dict())
    

def get_profile(request):
    '''获取个人资料'''
    # 中间件+@property+用户资料绑定在实例上
    profile_data = request.user.profile.to_dict()

    return render_json(code=stat.OK, data=profile_data)

def set_profile(request):
    """修改个人资料"""
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)

   
    # 检查User数据,is_valid:当不含有不合规的字段时是True,含不合规的字段时是False
    # 不合规的字段保存在user_form.errors里面
    if not user_form.is_valid():
        return render_json(code=stat.USER_DATA_ERROR, data=user_form.errors)

    # 检查Profile数据
    if not profile_form.is_valid():
        return render_json(code=stat.PROFILE_DATA_ERROR, data=profile_form.errors)
    
    #实例化绑定在request上的用户
    user = request.user
    # 保存用户数据，表单的所有数据保存在cleaned_data 里面
    user.__dict__.update(user_form.cleaned_data)
    user.save()

    # 保存交友资料数据
    user.profile.__dict__.update(profile_form.cleaned_data)
    user.profile.save()
    # user.profile.__dict__.update(profile_form.cleaned_data)
    # user.profile.save()

    return render_json()

def upload_avatar(requrst):
    '''上传个人形象'''
    return render_json()

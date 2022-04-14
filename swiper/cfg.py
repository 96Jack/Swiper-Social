"""程序逻辑配置个第三方平台配置: 相当于全局变量"""


from email.policy import default
from urllib.parse import urlencode


# Redis的相关配置

REDIS = {
        'host': '127.0.0.1',
        'port': 6379,
        'db'  : 3
}

# 滑动积分配置
SWIPER_SCORE = {
        'like': 5,
        'superlike': 7,
        'dislike': -5
}

# 反悔相关的配置
DAILY_REWIND = 3 # 每日可反悔的数目
REWIND_TIMEOUT = 5 * 60 # 可反悔记录的秒数


# 七牛云配置
QN_ACCESS_KEY = 'uQeKv_jRYUP8iz1g3uTv5LSwCSxIjysgUdwtv3Pt'
QN_SECRET_KEY = 'qZaNECJFH-3L2mNB7NHVlNFNDSz5R5ScaGKSZuCd'
QN_BASE_URL = 'http://py4hx1gc8.bkt.clouddn.com'
QN_BUCKET = 'th-test'




YZX_API = "https://open.ucpaas.com/ol/sms/sendsms"
YZX_ARGS = {
        "sid":"b8986f9d2717e385ac5f705b1ffec443",
        "token":"2f16a331eca3d8892e665afdc0224e52",
        "appid":"4f73ec27a7b54221b7dca9ee4f0def9b",
        "templateid":"154501",
        "param":"None",
        "mobile":"None",
}


# 微博配置
# ex: https://api.weibo.com/oauth2/authorize?client_id=123050457758183&redirect_uri=
# http://www.example.com/response&response_type=code
WB_APP_KEY = "3474883573"
WB_APP_SECRET = "c61135248ab7f3a30e121f95c0e68dfe"
WB_CALLBACK = "http://123.57.232.108:8000/weibo/callback"

# 第一步： Authorize 接口：第三方登录微博

WB_AUTH_API = 'https://api.weibo.com/oauth2/authorize'
WB_AUTH_ARGS = {
        'client_id': WB_APP_KEY,
        'redirect_uri': WB_CALLBACK,
        'display':default,
}
# 转译&；用？拼接url
WB_AUTH_URL = '%s?%s' % (WB_AUTH_API, urlencode(WB_AUTH_ARGS))
# print('+++++++WB_AUTH_URL :{}'.format(WB_AUTH_URL))

# 第二步access_token 接口： 获取微博服务器用户信息
WB_ACCESS_TOKEN_API = 'https://api.weibo.com/oauth2/access_token'
WB_ACCESS_TOKEN_ARGS = {
        'client_id': WB_APP_KEY,
        'client_secret': WB_APP_SECRET,
        'grant_type' : 'authorization_code',
        'redirect_uri':WB_CALLBACK,
        'code' : None 
}
# 获取用户信息
WB_USER_SHOW_API = 'https://api.weibo.com/2/users/show.json'
WB_USER_SHOW_ARGS = {
        'access_token' : None,
        'uid':None
}
"""放置程序逻辑中的状态码"""

OK = 0


class LogicErr(Exception):
    code = OK
    data = None

    def __init__(self, data=None ):
        # 当默认返回的数据无值时，返回异常的名字
        self.data = data or self.__class__.__name__

def gen_logic_err(name, code):
    """生成一个异常类"""
    # type(object_or_name, bases, dict)
    # 元类type创建类，类创建实例
    # (LogicErr, )元组， 类的多继承
    return type(name, (LogicErr, ), {'code':code}) 

nvildVcode        = gen_logic_err('InvildVcode', 10001)           # 验证码无效
AccessTokenError  = gen_logic_err('AccessTokenError', 1002)       # 授权码接口错误
UserInfoError     = gen_logic_err('UserInfoError', 1003)          # 用户信息接口错误
LoginRequired     = gen_logic_err('LoginRequired', 1004)          # 用户未登录
UserDataError     = gen_logic_err('UserDataError', 1005)          # 用户数据错误
ProfileDataError  = gen_logic_err('ProfileDataError', 1006)       # 用户交友资料错误
SwiperTypeError   = gen_logic_err('SwiperTypeError', 1007)        # 滑动类型错误
SwiperRepeatError = gen_logic_err('SwiperRepeatError', 1008)      # 重复滑动错误
RewindLimit       = gen_logic_err('RewindLimit', 1009)            # 反悔达到上限
RewindTimeout     = gen_logic_err('RewindTimeout', 1010)          # 反悔超时
Permissionlimit   = gen_logic_err('Permissionlimit', 1011)        # 用户没有相应的权限

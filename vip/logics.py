from common import stat


def need_permission(view_func):
    """权限检查装饰器"""
    def check(request, *args, **kwargs):
        perm_name = view_func.__name__

        # 检查当前用户是否具有所操作的函数对应的权限: 权限表的字段name保存权限名称与api接口函数名相同
        if request.user.vip.has_perm(perm_name):
            return view_func(request, *args, **kwargs)
        else:
            raise stat.Permissionlimit

    return check
    

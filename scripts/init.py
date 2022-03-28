from mimetypes import init
import os
import sys
import random
from datetime import date

import django



# 设置Django的运行环境
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')
django.setup()

# 加载django框架中的文件，要放在初始化django环境之后

from user.models import User 
from vip.models import Permission, VipPermRelation
from vip.models import Vip

print(BASE_DIR)

last_names = (

    '赵钱孙李周吴郑王'
    '冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张'
    '孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章'
    '云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方'
    '俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤'
    '滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康'
    '伍余元卜顾孟平黄'
    '和穆萧尹姚邵湛汪'
    '祁毛禹狄米贝明臧'
    '计伏成戴谈宋茅庞'
    '熊纪舒屈项祝董梁'
    '杜阮蓝闵席季麻强'
    '贾路娄危江童颜郭'
    '梅盛林刁钟徐邱骆'
)

first_names = {
    'male' : [
        '新奥','啸','洋','银易','基久','鼎','悦','宜英','先系','江','振','奥正','顺湖',
        '高精','凌','汇','鼎丰','惠湖','至','江','超利','曼真','网','中','阳太','尚事',
        '运光','太','南','士星','阳生','腾','飞','尚旭','诗广','诚','奇','莱迪','南诚',
        '英苏','博','越','飞先','龙真','中','翔','贵贝','振正','顺','亚','森蓝','京纳',
        '系爱','迪','浩','丰联','振智','营','诗','福曼','大铁','志','信','苏名','扬旋',
        '复天','诗','辉','坚浩','庆长','讯','开','邦网','振新','速','旋','广特','健生',
        '丝基','盛','旋','伟东','尼长','荣','耀','凤航','西奇','优','吉','拓大','维禾',
        '开语','川','辰','新霆','豪彩','娇','巨','川飞','恒磊','丰','立','飞星','正湖',
        '利速','宜','蓝','辉恒','磊码','瑞','展','伟苏','蓝日','博','码','诺微','正茂',
        '汉霸','鸿','惠','跃建','恒啸','频','科','木圣','鑫全','聚','艾','圣联','远禾',
        '越子','悦','铭','豪德','大邦','福','辉','旭鑫','斯电','星','伟','顿茂','欧长',
    ],
    'female':[
        '冠丝','纽腾','隆','洁','越明','嘉邦','晶','泰','讯艾','安','龙','时泰','庆瑞',
        '事精','尚德','易','龙','盈风','庆良','营','太','巨运','亿','韦','联亿','安欧',
        '火妙','安维','赛','森','成远','广复','用','帝','洁嘉','诺','盛','缘银','高明',
        '源浩','润霸','冠','丰','长思','理福','新','语','圣韦','星','航','开网','苏精',
        '清巨','白傲','辉','展','高惠','开达','南','磊','富傲','和','纳','全日','丝集',
        '卓用','升立','百','信','超瑞','悦妙','特','奥','蓝辰','罗','力','雅易','银贸',
        '硕康','宏妙','精','玉','巨冠','安罗','缘','康','理永','百','本','邦讯','坚金',
        '斯耀','东仕','丝','纽','扬精','爱频','事','顺','清复','霸','集','帝胜','易南',
        '森欧','具宏','识','用','复志','立春','润','永','坚禾','苏','电','界派','驰宝',
        '开讯','特网','理','好','迪西','祥原','倍','洁','基宏','双','胜','万大','本纳',
        '京本','悦鼎','鑫','迎','联太','盛财','拓','财','英光','旺','益','白胜','亚宏',
        '运恒','倍泰','福','嘉','码森','鼎派','明','久','腾银','迎','银','运特','界网',
    ]
}
def random_name():
    """随机产生一个名字"""
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name, first_name]), sex

def create_robots(n):
    # 创建初始用户
    for i in range(n):
        name, sex = random_name()
        try:
            year = random.randint(1970, 2000)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            # User = Models.User
            user_ = User.objects.create(
                phonenum = '%s' % random.randrange(21000000000, 21900000000),
                nickname = name,
                sex = sex,
                birth_day = date(year, month, day),
                location = random.choice([item[0] for item in User.LOCATION]),
            )
            print('creates: %s %s %s ' % (user_.id, name, sex))
        except django.db.utils.IntegrityError:
            pass

def init_permission():
    """创建权限模型"""
    permissions = (
        ('vipflag',             '会员身份标识'),
        ('superlike',           '超级喜欢'),
        ('rewind',              '反悔功能'),
        ('anylocation',         '任意更改定位'),
        ('unlimit_like',        '无限喜欢次数'),
        ('show_liked_me',       '查看喜欢过我的人'),
    )

    for name, desc in permissions:
        perm, _ = Permission.objects.get_or_create(name=name, desc=desc)
        print('create permission %s' % perm.name)

def init_vip():
    duration = {
        0: 100000, 
        1: 60, 
        2: 50, 
        3: 30, 
    }
    for i in range(4):
        vip, _ = Vip.objects.get_or_create(
            name  ='%d 级会员' % i , 
            level = i , 
            price = i * 10.0, 
            days = duration[i], 
        )
        print('create %s' % vip.name)

def create_vip_perm_relations():
    """创建Vip和Permission的关系"""
    # 获取VIP
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    # 获取权限
    vipflag         =        Permission.objects.get(name      ='vipflag')
    superlike       =        Permission.objects.get(name      ='superlike')
    rewind          =        Permission.objects.get(name      ='rewind')
    anylocation     =        Permission.objects.get(name      ='anylocation')
    unlimit_like    =        Permission.objects.get(name      ='unlimit_like')
    show_liked_me   =        Permission.objects.get(name      ='show_liked_me')

    # 给VIP 1 分配权限
    VipPermRelation.objects.get_or_create(vip_id=vip1.id, perm_id=vipflag.id )
    VipPermRelation.objects.get_or_create(vip_id=vip1.id, perm_id=superlike.id )

    # 给VIP 2 分配权限
    VipPermRelation.objects.get_or_create(vip_id=vip2.id, perm_id=vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id=vip2.id, perm_id=superlike.id)
    VipPermRelation.objects.get_or_create(vip_id=vip2.id, perm_id=rewind.id)

    # 给VIP 3 分配权限
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=vipflag.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=superlike.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=rewind.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=anylocation.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=unlimit_like.id)
    VipPermRelation.objects.get_or_create(vip_id=vip3.id, perm_id=show_liked_me.id)


if __name__=="__main__":
    create_robots(10000)
    # init_permission()
    # init_vip()
    # create_vip_perm_relations()

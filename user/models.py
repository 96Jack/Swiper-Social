from random import choices
from django.db import models

# Create your models here.

class User(models.Model):
    # 提供可选项，元组，前面一个值存在数据库，后面的值时提示用
    SEX = (
        ('male',   '男性'),
        ('female', '女性')
    )
    LOCATION = (
        ('北京',('北京')),
        ('上海',('上海')),
        ('深圳',('深圳')),
        ('广州',('广州')),
        ('重庆',('重庆')),
        ('西安',('西安')),
        ('武汉',('武汉')),
        ('沈阳',('沈阳')),
    )
    phonenum      = models.CharField(max_length=15, unique=True, verbose_name="⼿机号     ")
    nickname      = models.CharField(max_length=20, verbose_name="昵称 ")
    sex           = models.CharField(max_length=8, choices=SEX, verbose_name="性别  ")
    # birth_year    = models.CharField( verbose_name="出⽣年")
    # birth_month   = models.CharField( verbose_name="出⽣⽉    ")
    birth_day     = models.DateField(max_length=8, default='1990-1-1', verbose_name="出⽣⽇    ")
    # 形象介绍的内容较多，一般存在服务器，给网址
    avatar        = models.CharField( max_length=256, verbose_name="个⼈形象   ")
    location      = models.CharField( max_length=20, choices=LOCATION, verbose_name="常居地         ")
             
    '''
    User 和 Profile 之间是一对一的关系:不使用外键构建一对一表关系
    1.通过id绑定User和Profile两表之间的关系,不使用外键,性能太差
    2.将获取用户资料的函数profile属性化,可以通过实例名来调用
    3.get_or_create()先获取,若获取不到则创建
    4.将获取的用户资料绑定在实例身上,避免每次获取用户资料都要去数据库获取数据,性能不好
    '''
    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


    def to_dict(self):
        return {
             "id"            : self.id,
             "phonenum "     : self.phonenum,
             "nickname "     : self.nickname,
             "sex      "     : self.sex,
             # 将datetime.date 类型转换成str
             "birth_day"     : str(self.birth_day),
             "avatar   "     : self.avatar,
             "location "     : self.location,
}


class Profile(models.Model):
    '''交友资料'''

    dating_sex        = models.CharField(max_length=8, choices=User.SEX, verbose_name='匹配的性别'  )
    dating_location   = models.CharField(max_length=20, choices=User.LOCATION, verbose_name= '⽬标城市'   )
    min_dating_age    = models.IntegerField(default=18, verbose_name='最⼩交友年龄'  )
    max_dating_age    = models.IntegerField(default=50,  verbose_name='最⼤交友年龄' )
    min_distance      = models.IntegerField(default=1,  verbose_name='最⼩查找范围'  )
    max_distance      = models.IntegerField(default=30,  verbose_name='最⼤查找范围' )
    vibration         = models.BooleanField(default=True,  verbose_name='开启震动')
    only_matche       = models.BooleanField(default=True,  verbose_name='只让匹配的⼈看我的相册')
    auto_play         = models.BooleanField(default=True,  verbose_name='⾃动播放视频')

    def to_dict(self):
        return {
            "id"                :    self.id   , 
            "dating_sex"        :    self.dating_sex   ,         
            "dating_location"   :    self.dating_location ,                
            "min_dating_age"    :    self.min_dating_age ,               
            "max_dating_age"    :    self.max_dating_age ,               
            "min_distance"      :    self.min_distance  ,            
            "max_distance"      :    self.max_distance  ,            
            "vibration"         :    self.vibration     ,      
            "only_matche"       :    self.only_matche   ,          
            "auto_play"         :    self.auto_play     ,      


        }



import os
import django

# 不可单独加载Django环境，引入Django环境设置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings' )
django.setup()

from user.models import User

users = User.objects.all()
print(users)

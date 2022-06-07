"""
Django settings for swiper project.

Generated by 'django-admin startproject' using Django 1.11.24.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(f"=====BASE_DIR:{BASE_DIR}======")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hq)cfxev39@24&3^-d!z=d5^dv&t_13h^inbkpfkd%^y88#r#!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'social',
    'vip',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自定义中间件
    'common.middleware.AuthorizeMiddleware',
    # 'common.middleware.LogicErrMiddleware',
]

ROOT_URLCONF = 'swiper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'swiper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'swiper',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456'
    }

}

# 让Django使用 Redis作为缓存后端：
#       1. pip install django-cache  
#       2.freeze > requirement.txt
# from django.core.cache import cache 此时就会用redis作为缓存使用:
#       from django.conf import settings 查看
# 无cache.range() : 
#       只封装了redis缓存的接口，不能代替redis,
#       使用redis更高级的语法得用封装的接口
CACHES = {
    'default':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://172.18.0.1/3',
        'OPTIONS':{
            'CLIENT_CLASS':"django_redis.client.DefaultClient",
            'PICKLE_VERSION':-1,
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# 日志配置
LOGGING = {
    'version':1,
    'disable_existing_loggers': False, # 关闭django里面的其他日志
    # 格式配置
    'formatters':{
        'simple':{
            'format':'%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt':'%Y-%m-%d %H:%M:%S',
        },
        'verbose':{
            'format':('%(asctime)s %(levelname)s [%(process)d-%(threadName)s]'
                    '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt':'%Y-%m-%d %H:%M:%S',
        }
    },

    #handler 配置
    'handlers':{
        'console':{
            'class': 'logging.StreamHandler',
            'level': 'DEBUG' if DEBUG  else 'WARNING'
        },
        'info':{
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # f'variable_name' : 直接会将指定的变量内容拼进字符串
            'filename': f'{BASE_DIR}/logs/info.log', # 日志保存路径
            'when': 'D',                             # 每天切割日志
            'backupCount':30,                        # 日志的保留时间
            'formatter': 'simple',
            'level':    'INFO',
        },
        'error':{
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/error.log', # 日志保存路径
            'when': 'W0',                             # 每周一切割日志（周二：W1）
            'backupCount':4,                          # 日志的保留时间
            'formatter': 'verbose',
            'level':    'WARNING',
        }
    },
    # Logger 配置
    'loggers':{
        'django':{
            'handlers':['console'],
        },
        'inf':{
            'handlers':['info'],
            'propagate':True,
            'level': 'INFO',
        },
        'err':{
            'handlers':['error'],
            'propagate':True,
            'level': 'WARNING',
        }
    }
}



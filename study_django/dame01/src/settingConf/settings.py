
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# import sys
# sys.path.insert(1, os.path.join(BASE_DIR, 'core'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0cgjo+57we)d&x1kp%@1q8_!^(+si^h%x+)86hqwc9r+@x!qf#'


AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core.apps.CoreConfig',
    'captcha',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware'
]


AUTH_USER_MODEL = "core.User"
ROOT_URLCONF = 'settingConf.urls'
WSGI_APPLICATION = 'settingConf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm',
        'HOST': '192.168.132.77',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'mysql',
    }
}




# 邮件发送设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务器地址
EMAIL_HOST = 'smtp.163.com'
# SMTP服务端口
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'zhangjunbo0405@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = '1234567qwerty'
# 收件人看到的发件人
EMAIL_FROM = '最上川<zhangjunbo0405@163.com>'

# # 字母验证码
# CAPTCHA_IMAGE_SIZE = (80, 45)  # 设置 captcha 图片大小
# CAPTCHA_LENGTH = 4  # 字符个数
# CAPTCHA_TIMEOUT = 1  # 超时(minutes)
# APTCHA_BACKGROUND_COLOR = '#ffffff'
#
#
# # 加减乘除验证码
# CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
# CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',  # 没有样式
#                            'captcha.helpers.noise_arcs',  # 线
#                            'captcha.helpers.noise_dots',  # 点
#                            )
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'   # 图片中的文字为随机英文字母，例如mdsh
# # CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# # CAPTCHA_CHALLENGE_FUNCT ='captchachallenge'  #文字为数字表达式，如1 + 2 = </ span>


#字母验证码
CAPTCHA_IMAGE_SIZE = (800, 450)   # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4   # 字符个数
CAPTCHA_TIMEOUT = 10   # 超时(minutes)

#加减乘除验证码
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null',
     'captcha.helpers.noise_arcs', # 线
     'captcha.helpers.noise_dots', # 点
)

# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'


BASE_URL = 'http://192.168.132.77:8886/api/v1/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

STATIC_URL = '/STATIC/'



import datetime

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),

    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # )

    # 异常处理
    'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',


}
JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000000),
}

# CORS跨域请求的白名单
CORS_ORIGIN_WHITELIST = (
    '192.168.132.77:8887',
    'www.zsc.site:8887',
)

# Django缓存设置（如果不做设置，Django缓存默认是服务器内存)
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 存储短信验证码的内容
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 存储浏览商品记录
    "histories": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 存储购物车记录
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

}
# Django的session存储设置(把session存储缓存中，因为缓存已经设置为了redis，所以session就存储到redis中)
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# session存储到缓存空间的名称
SESSION_CACHE_ALIAS = "session"





# REST_FRAMEWORK = {
#     # 全局认证的匿名类, 也可以单个使用
#     'DEFAULT_AUTHENTICATION_CLASSES': ["libs.auth.FirstAuthentication", "libs.auth.Authtication"],
#     # 匿名用户登陆
#     # 'DEFAULT_AUTHENTICATION_CLASSES': ["libs.auth.FirstAuthentication"],
#     # 'UNAUTHENTICATED_USER': None,  # 用户为匿名用户或者未登录，request.user = None
#     # 'UNAUTHENTICATED_TOKEN': None, # 用户为匿名用户或者未登录，request.auth = None
#
#     # 权限认证
#     'DEFAULT_PERMISSION_CLASSES': ['libs.permission.MyPermission', 'libs.permission.MyPermission2',],
#     # 配置访问频率
#     'DEFAULT_THROTTLE_CLASSES': ['libs.throttle.VisitThrottle'],
#     # 内部上面加下面
#     'DEFAULT_THROTTLE_RATES': {
#         "Luffy": "3/m",   # 未登录访问频率
#         "LuffyUser": "5/m"  # 已登录访问频率
#     },
#
#
# #     'DEFAULT_PERMISSION_CLASSES': (
# #         'rest_framework.permissions.IsAuthenticated',
# #     ),
# #
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     ),
#     'DEFAULT_PARSER_CLASSES': (
#         'rest_framework.parsers.JSONParser',
#     ),
#
#     'PAGE_SIZE': 10
# }
#
# import datetime
#
# # 用户认证插件
# JWT_AUTH = {
#     'JWT_RESPONSE_PAYLOAD_HANDLER':
#         'rest_framework_jwt.utils.jwt_response_payload_handler',
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000000),
# }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/crm.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    }
}






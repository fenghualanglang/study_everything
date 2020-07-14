


# celeryconfig.py

RABBIT_MQ = {
    'HOST': '106.13.168.8',
    'PORT': 15672,
    'USER': 'guest',
    'PASSWORD': 'guest'
}

'http://106.13.168.8:15672/#/'

CELERY_IMPORTS = ("rocket.tasks", )

BROKER_URL = 'amqp://%s:%s@%s:%s/myvhost' % (RABBIT_MQ['USER'], RABBIT_MQ['PASSWORD'], RABBIT_MQ['HOST'], RABBIT_MQ['PORT'])
BACKEND_URL = 'amqp://myuser:mypassword@localhost/myvhost'

# CELERYD_LOG_FORMAT = '[%(asctime)s] [%(levelname)s] %(message)s'
CELERY_ROUTES = {
        'celery_tasks.tasks.add': {'queue': 'sunday'},
}


print(CELERY_IMPORTS)

print(BROKER_URL)

# print(CELERYD_LOG_FORMAT)

print(CELERY_ROUTES)





# 其中，参数定义如下：
# CELERY_IMPORTS 导入的task
# BROKER_URL指定了broker信息，即消息队列的地址。
# CELERYD_LOG_FORMAT 指定了日志格式。
# CELERY_ROUTES 指定了路由信息，即调用rocket.tasks.add后，消息具体放入哪个队列，这里是队列名称为sunday。















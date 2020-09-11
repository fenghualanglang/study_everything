# -*- coding:utf-8 -*-

from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://:123456@106.13.168.8:6379/12' # Broker配置，使用Redis作为消息中间件

CELERY_RESULT_BACKEND = 'redis://:123456@106.13.168.8:6379/13' # BACKEND配置，这里使用redis

CELERY_RESULT_SERIALIZER = 'json' # 结果序列化方案

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间

CELERY_TIMEZONE='Asia/Shanghai'   # 时区配置

CELERY_IMPORTS = (     # 指定导入的任务模块,可以指定多个
    "celery_proj.add_task.tasks",
    'celery_proj.sms_task.tasks',
)
CELERYBEAT_SCHEDULE = {
    'add': {          # 每10秒执行
        'task': 'celery_proj.add_task.tasks.add',  #任务路径
        'schedule': 30.0,
        'args': (10,12),
    },
    'sayhi': {          # 每10秒执行
        'task': 'celery_proj.sms_task.tasks.sayhi',  #任务路径
        'schedule': 16.0,
        'args': ('wd',),
    },
    'sum': {          # 每10秒执行
        'task': 'celery_proj.add_task.tasks.sum',  #任务路径
        'schedule': timedelta(seconds=30),  # 每 30 秒执行一次
        'args': (1,3),
    },
}



'''
CELERY_TIMEZONE 配置celery时区
CELERY_ENABLE_UTC 是否启动UTC时间
CELERYD_MAX_TASKS_PER_CHILD 配置worker执行多少任务后kill掉
CELERY_IMPORTS 默认导入的任务文件名（最好不要改动）
imports 导入定时任务celery5  imports = ["tasks.message_task",]
test1 随意定义
test1_run 任务名
'''
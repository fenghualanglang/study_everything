# -*- coding: utf-8 -*-

from datetime import timedelta
from celery.schedules import crontab

# Broker配置，使用Redis作为消息中间件
BROKER_URL = 'redis://:123456@106.13.168.8:6379/14'

# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = 'redis://:123456@106.13.168.8:6379/15'

# 时区
CELERY_TIMEZONE='Asia/Shanghai'
# 是否使用UTC, 默认不指定
CELERY_ENABLE_UTC = False

# 配置worker执行多少任务后kill掉
# CELERYD_MAX_TASKS_PER_CHILD = 10

# 结果序列化方案
# CELERY_RESULT_SERIALIZER = 'json'

# 任务过期时间
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# 导入定时任务
CELERY_IMPORTS = (
    "celery_app.add_task.tasks",
    "celery_app.sms_task.tasks"
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {     # 计划任务
        'task': 'celery_app.add_task.tasks.add',   # 任务路径
         'schedule': timedelta(seconds=30),        # 每 30 秒执行一次
         'args': (5, 8)                            # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.sms_task.tasks.send_sms',
        'schedule': timedelta(seconds=40),  # 每 30 秒执行一次
        # 'schedule': crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
        'args': ('18019186564', )                 # 任务函数参数
    }
}




#!/usr/bin/python3.6
from datetime import timedelta

from celery.schedules import crontab
from kombu import Exchange, Queue

# 使用RabbitMQ作为消息代理
BROKER_URL = "amqp://guest:guest@106.13.168.8:5672/my_host"
# 把任务结果存在了Redis
CELERY_RESULT_BACKEND = "redis://:123456@106.13.168.8:6379/7"

CELERY_TIMEZONE = "Asia/Shanghai"  # 时区设置

# 任务序列化
CELERY_TASK_SERIALIZER = "json"
# 任务执行结果序列化
CELERY_RESULT_SERIALIZER = "json"
# 设置存储的过期时间　防止占用内存过多
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 指定了日志格式
# CELERYD_LOG_FORMAT = '[%(asctime)s] [%(levelname)s] %(message)s'
CELERY_ACCEPT_CONTENT = ['json'] # 指定接受的内容类型


CELERY_DEFAULT_QUEUE = 'web_tasks'  # 默认的队列
# CELERY_DEFAULT_EXCHANGE = 'distribution'  # 默认的交换机名字为
# CELERY_DEFAULT_EXCHANGE_TYPE = 'topic' # 默认的交换类型是topic
# CELERY_DEFAULT_ROUTING_KEY = 'task.default' # 默认的路由键是task.default，这个路由键符合上面的default队列



CELERY_QUEUES = (
    # 路由键以'web.'开头的消息都进web_tasks队
    Queue('web_tasks',  Exchange('web_tasks', 'topic'), routing_key='web.#'),

    # Queue('manual_task', Exchange('celery_task'), routing_key='manual_task', queue_arguments={'max_priority': 7})
)

# 在出现worker接受到的message出现没有注册的错误时，引入任务列表
CELERY_IMPORTS = ['celery_tasks.email_tasks.tasks', 'celery_tasks.sms_tasks.tasks']

CELERY_ROUTES = {
    # tasks.add的消息会进入web_tasks队列
    'email_tasks.tasks.send_email': {'queue': 'web_tasks', 'routing_key': 'web.send_email', },
    'sms_tasks.tasks.send_sms': {'queue': 'web_tasks', 'routing_key': 'web.send_sms', },

    # 'tasks.manual_task': {'exchange': 'celery_task', 'routing_key': 'manual_task', 'priority': 7},
}


# 定时任务
CELERYBEAT_SCHEDULE = {
    "send_sms-every-30-seconds": {
        "task": "celery_tasks.sms_tasks.tasks.send_sms",
        "schedule":timedelta(seconds=30),
        "args": ("python", "18236766280"),
    },
}


# task_acks_late属性设置Worker被关闭重启后能够继续执行之前没完成的任务
# task_track_started会显示正在执行的任务状态为STARTED，而不是PENDING
# worker_prefetch_multiplier节点预取倍数
# worker_concurrency并发处理任务数

# 限制执行频率
# CELERY_ANNOTATIONS = {
#     "celery_tasks.tasks.send_sms": {"rate_limit": "1/m"},
#     "celery_tasks.tasks.send_email": {"rate_limit": "1/m"}
# }



#!/usr/bin/python3.6
from kombu import Exchange, Queue

# 需要按照celery格式
BROKER_URL = "redis://:123456@106.13.168.8:6379/3"
# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = "redis://:123456@106.13.168.8:6379/4"

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"


CELERY_IMPORTS = ['celery_demo.email_tasks.tasks', ]

# CELERY_DEFAULT_QUEUE = 'default'   # 设置默认的路由
# CELERY_DEFAULT_EXCHANGE = 'default'
# CELERY_DEFAULT_ROUTING_KEY = 'default'


CELERY_QUEUES = {
    # Queue("default", Exchange("default"), routing_key=("default")),
    Queue("email", Exchange("for_email_task"), routing_key=("for_email_task")),

    # Queue("mix_add_task", Exchange("for_mix_add_task"), routing_key=("for_mix_add_task")),
    #
    # Queue("manual_task", Exchange("celery_task"), routing_key="manual_task", queue_arguments={"max_priority": 9}),
    # Queue("semi_auto_task", Exchange("celery_task"), routing_key="for_semi_auto_task", queue_arguments={"max_priority": 8}),
    # Queue("auto_task", Exchange("celery_task"), routing_key="for_auto_task", queue_arguments={"max_priority": 7}),
    # Queue("scheduler", Exchange("celery_task"), routing_key="for_scheduler", queue_arguments={"max_priority": 7}),
}

CELERY_ROUTES = {
    "email_tasks.tasks": {"queue": "email", "routing_key": "for_email_task"},
    # "tasks.mix_add_task": {"queue": "for_mix_add_task", "routing_key": "for_mix_add_task"},
    #
    # "tasks.manual_task": {"queue": "for_manual_task", "routing_key": "for_manual_task"},
    #
    # "tasks.semi_auto_task": {"queue": "celery_task", "routing_key": "for_semi_auto_task", "priority": 7},
    # "tasks.auto_task": {"queue": "celery_task", "routing_key": "for_auto_task", "priority": 1},
    # "tasks.scheduler": {"queue": "celery_task", "routing_key": "for_scheduler", "priority": 1}
}



# # celery定时任务
# CELERY_TIMEZONE = "UTC"
# CELERYBEAT_SCHEDULE = {
#     "taskA_schedule": {
#         "task": "tasks.add_task",
#         "schedule": 20,
#         "args": (5, 6)
#     },
#     "taskB_schedule": {
#         "task": "tasks.mix_add_task",
#         "schedule": 50,
#         "args": (100, 200, 300)
#     },
#     "add_schedule": {
#         "task": "tasks.manual_task",
#         "schedule": 10,
#         "args": (10, 20)
#     }
# }
#












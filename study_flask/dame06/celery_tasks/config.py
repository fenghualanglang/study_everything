# -*- coding:utf-8 -*-
from kombu import Exchange, Queue

BROKER_URL = 'redis://:123456@106.13.168.8:6379/3'

# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = 'redis://:123456@106.13.168.8:6379/4'


CELERY_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("send_email", Exchange("send_email"), routing_key="send_email"),
    Queue("sms_task", Exchange("sms_task"), routing_key="sms_task")
)

# 路由
CELERY_ROUTES = {
    'celery_tasks.email_task.tasks': {"queue": "send_email", "routing_key": "send_email"},
    'celery_tasks.sms_task.tasks': {"queue": "sms_task", "routing_key": "sms_task"}
}




# CELERY_DEFAULT_QUEUE = 'default'  # 设置默认的路由
# CELERY_DEFAULT_EXCHANGE = 'default'
# CELERY_DEFAULT_ROUTING_KEY = 'default'
# CELERY_TASK_RESULT_EXPIRES = 10  # 设置存储的过期时间　防止占用内存过多


# from kombu import Exchange, Queue
# from routers import MyRouter
#
# # 配置市区
# CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_BROKER = 'amqp://localhost'
#
# # 定义一个默认交换机
# default_exchange = Exchange('dedfault', type='direct')
#
# # 定义一个媒体交换机
# media_exchange = Exchange('media', type='direct')
#
# # 创建三个队列，一个是默认队列，一个是video、一个image
# CELERY_QUEUES = (
    # Queue('default', default_exchange, routing_key='default'),
    # Queue('videos', media_exchange, routing_key='media.video'),
    # Queue('images', media_exchange, routing_key='media.image')
# )
#
# CELERY_DEFAULT_QUEUE = 'default'
# CELERY_DEFAULT_EXCHANGE = 'default'
# CELERY_DEFAULT_ROUTING_KEY = 'default'
#
# CELERY_ROUTES = (
#     {
#         'tasks.image_compress': {
#             'queue': 'images',
#             'routing_key': 'media.image'
#         }
#     },
#     {
#         'tasks.video_upload': {
#             'queue': 'videos',
#             'routing_key': 'media.video'
#         }
#     },
#     {
#         'tasks.video_compress': {
#             'queue': 'videos',
#             'routing_key': 'media.video'
#         }
#     }
# )
#
# # 在出现worker接受到的message出现没有注册的错误时，使用下面一句能解决
# CELERY_IMPORTS = ("tasks",)

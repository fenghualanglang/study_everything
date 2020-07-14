# celery 配置文件

from celery import Celery

backend = 'amqp://guest:guest@106.13.168.8:15672/tt'
broker= 'amqp://guest:guest@106.13.168.8:15672/tt'

app = Celery(
    'test',
    backend=backend,
    broker=broker,
    include=['celery_tasks.tasks01', 'celery_tasks.tasks02']
)

# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False



#dame2      celery worker -A celery_tasks -l info -P eventlet

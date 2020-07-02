# celery 配置文件

from celery import Celery


backend = 'redis://:1qaz2wsx@192.168.43.187:6379/1'
broker = 'redis://:1qaz2wsx@192.168.43.187:6379/2'

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

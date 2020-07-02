from celery import Celery
import time


backend = 'redis://:1qaz2wsx@192.168.43.187:6379/1'
broker = 'redis://:1qaz2wsx@192.168.43.187:6379/2'

app = Celery('test',backend=backend,broker=broker)


@app.task
def send_email(name):
    print('向%s发送邮件' % name)
    time.sleep(3)
    print('向%s发送邮件完成' % name)
    return 'OK'


@app.task
def send_msg(name):
    print('向%s发送短信' % name)
    time.sleep(3)
    print('向%s发送短信完成' % name)
    return 'OK'


# celery worker -A celery_task -l info
















import time
from celery_tasks.celery import app

@app.task
def send_msg(name):
    print('向%s发送短信' % name)
    time.sleep(3)
    print('向%s发送短信完成' % name)
    return 'OK'

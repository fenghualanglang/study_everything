
import time
from celery_tasks.celery import app

@app.task
def send_email(name, sex):
    print(f'向{name}发送{sex}邮件')
    time.sleep(5)
    print('向%s发送邮件完成' % name)
    return '邮件完成'
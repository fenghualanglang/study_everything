import random
import requests

from celery_tasks.main import app, logger


@app.task
def send_sms(username, phone):
    logger.info('task id:{} , arg:{} , successful !'.format(username, phone))
    return 'task id:{} , arg:{} , successful !'.format(username, phone)
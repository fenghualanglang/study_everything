

import random
import requests

from celery_tasks.main import app, logger


@app.task
def send_email(username, email):
    logger.info('task id:{} , arg:{} , successful !'.format(username, email))
    return 'task id:{} , arg:{} , successful !'.format(username, email)








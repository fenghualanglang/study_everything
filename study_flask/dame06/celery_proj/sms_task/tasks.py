
from celery_proj.main import app, log
from celery_proj import TaskStatus


@app.task(base=TaskStatus)
def sayhi(name):
    a=[]
    return 'hi {}'.format(name)


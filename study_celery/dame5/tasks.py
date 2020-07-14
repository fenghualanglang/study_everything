from celery import Celery

app = Celery('tasks',broker='amqp://myuser:mypassword@localhost/myvhost',backend='amqp')

@app.task
def add(x,y):
    return x+y


# celery -A tasks worker -l info
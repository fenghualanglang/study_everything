import time
from celery import Celery

backend = 'amqp://guest:guest@106.13.168.8:15672/'
broker= 'amqp://guest:guest@106.13.168.8:15672/'

app = Celery('tasks', backend=broker, broker=broker)

@app.task
def add(x, y):
  time.sleep(5)
  return x + y
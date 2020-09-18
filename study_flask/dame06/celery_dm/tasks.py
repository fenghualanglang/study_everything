#!/usr/bin/python3.6

from celery import Celery
app = Celery()
app.config_from_object("config")

@app.task
def add_task(x, y):
    return x+y

@app.task
def mix_add_task(x, y, z):
    return x+y+z

@app.task
def multip_task(x, y):
    return x*y



# 手动执行任务
@app.task
def manual_task(a, b):
    # 手动执行任务
    return a+b
#
# 半自动执行任务
@app.task
def semi_auto_task(phone):
    return phone

# 自动执行任务
@app.task
def auto_task(email):
    return email

# 定时任务
@app.task
def scheduler(weather):
    return weather

#
#
#
#



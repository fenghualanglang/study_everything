from __future__ import absolute_import
# 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
import os
import sys

from celery import Celery
from celery.utils.log import get_task_logger

BASE_PARH = os.path.dirname(os.path.dirname(__file__))

# 增加日志记录 方便日志查找问题
log = get_task_logger(__name__)
sys.path.insert(0, BASE_PARH)

app = Celery("demo")
app.config_from_object("celery_demo.config")
# 定义的任务
app.autodiscover_tasks(["celery_demo.email_tasks","celery_demo.sms_tasks"])


'''
启动任务某个任务队列
celery -A main  worker -l info -Q send_tasks -P eventlet

定时任务-启动调度器
celery beat -A main -l info

定时任务-启动任务队列
celery -A main worker -l info -P eventlet
'''

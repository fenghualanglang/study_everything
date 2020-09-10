from __future__ import absolute_import
import os
import sys

from celery import Celery
from celery.utils.log import get_task_logger

BASE_PARH = os.path.dirname(os.path.dirname(__file__))

print(BASE_PARH)

# 增加日志记录 方便日志查找问题
log = get_task_logger(__name__)
sys.path.insert(0, BASE_PARH)

app = Celery("demo")
app.config_from_object("celery_app.config")
# 定义的任务
app.autodiscover_tasks(["celery_app.add_task", "celery_app.sms_task"])





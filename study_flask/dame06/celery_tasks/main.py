from __future__ import absolute_import
import os
import sys

from celery import Celery
from celery.utils.log import get_task_logger

BASE_PARH = os.path.dirname(os.path.dirname(__file__))

# 增加日志记录 方便日志查找问题
logger = get_task_logger(__name__)

sys.path.insert(0, BASE_PARH)

# 创建 Celery 实例
app = Celery("project_proj")

# 加载配置模块
app.config_from_object("celery_tasks.config")
# 定义的任务
app.autodiscover_tasks(["celery_tasks.email_task", "celery_tasks.sms_task"])


# celery beat -A  celery_proj.period_task -l  debug
# celery -A celery_proj worker  -l info -P eventlet
# celery -A celery_tasks.main worker -l info -n workerA%h -Q send_email -P eventlet




'''
sys.path.insert(0, BASE_PARH) 将当前路径添加到python环境变量，如果不导入其他自定义模块内容，可以忽略
capp.config_from_object(“tasks.config”) 以文件的方式配置celery
autodiscover_tasks 自动搜索任务，可以接收多个路径
'''
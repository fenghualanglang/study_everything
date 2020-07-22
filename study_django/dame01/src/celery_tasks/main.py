from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# 设置Django运行所依赖环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settingConf.settings")  # 设置django环境  manage.py
# 创建Celery类的对象
celery_app = Celery('celery_tasks')
# 加载配置
celery_app.config_from_object('celery_tasks.config')   # 使用CELERY_ 作为前缀，在settings中写配置

# app.autodiscover_tasks()  # 发现任务文件每个app下的task.py
# 让celery worker启动时自动发现有哪些任务函数
celery_app.autodiscover_tasks(['celery_tasks.email'])




from celery import Celery
#创建Celery对象
#参数main 设置脚本名
app = Celery('celery_tasks')
#加载配置文件
app.config_from_object('celery_tasks.config')
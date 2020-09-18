task_serializer = 'json' 

result_serializer = 'json' 

accept_content = ['json'] 

timezone = "Asia/Shanghai"  *# 时区设置* 

worker_hijack_root_logger = False  *# celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空* 

result_expires = 60 * 60 * 24  *# 存储结果过期时间（默认1天）* 

导入任务所在文件 

imports = [    "celery_task.epp_scripts.test1",    "celery_task.epp_scripts.test2"] 

from __future__ import absolute_import *# 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行* 





 celery worker  -A demo_task -Q sunday --loglevel=info  -f app.log 

- 参数`-A` 是app name,即定义celery的文件。
- 参数`-Q`指定了队列的名称，如果不指定，默认为`celery`。
- 参数`-f` 指定了日志打印文件。










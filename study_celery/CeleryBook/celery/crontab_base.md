**字段解释：**
task：需要执行的任务名称.如@app.task(name=‘schedule_add’),则’task’: ‘schedule_add’,
schedule：任务执行时间设定，使用crontab可以实现复杂的定时任务。如果要实现秒级定时任务，使用：‘schedule’: 10.0,
args：一个元组或者列表，位置参数
kwargs：一个字典，关键字参数
options：一个字典，一些额外选项，apply_async()方法可用的参数，exchange, routing_key, expires等
relative：默认false 

 **定时方式 **

```python
from celery.schedules import crontab
from datetime import timedelta

方式一：hours=xx,minutes=xx 每小时/每分钟 
"schedule": timedelta(seconds=30)

方式二：every 10 minutes
"schedule": crontab(minute="*/10"),   # every 10 minutes  
```

**启动定时器：**

 - 发布任务  `celery -A celery_task beat `

 - 执行任务  `celery -A celery_task worker --loglevel=info` 

 - 发布并执行 `celery -B -A celery_task worker --loglevel=info`  

- 发布任务 `celery beat -A tasks -l info -f logging/schedule_tasks.log`
  `-f logging/schedule_tasks.log`：定时任务日志输出路径

- 发布任务 后台运行 `celery beat -A tasks -l info -f logging/schedule_tasks.log --detach`

  `--detach`





```python
# 后台启动 celery worker进程 
celery multi start work_1 -A appcelery  
# work_1 为woker的名称，可以用来进行对该进程进行管理

# 多进程相关
celery multi stop WOERNAME # 停止worker进程,有的时候这样无法停止进程，就需要加上-A 项目名，才可以删掉
celery multi restart WORKNAME        # 重启worker进程

# 查看进程数
celery status -A celery_task       # 查看该项目运行的进程数   celery_task同级目录下

执行完毕后会在当前目录下产生一个二进制文件，celerybeat-schedule 。
该文件用于存放上次执行结果：
　　1、如果存在celerybeat-schedule文件，那么读取后根据上一次执行的时间，继续执行。
　　2、如果不存在celerybeat-schedule文件，那么会立即执行一次。
　　3、如果存在celerybeat-schedule文件，读取后，发现间隔时间已过，那么会立即执行。
```



 https://www.cnblogs.com/lanyangsh/p/10743035.html 

 https://blog.csdn.net/chenbogger/article/details/99308404 

 https://blog.csdn.net/weixin_39318540/article/details/80473021 
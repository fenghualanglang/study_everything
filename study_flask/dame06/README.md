### python app.py runserver -p 5001

#### 一版
`celery==3.1.24`
`redis == 2.10.6`
- 启动 Celery Worker 进程
    `celery -A celery_app worker --loglevel=info`
- 启动 Celery Beat 进程，定时将任务发送到 Broker 
    `celery beat -A celery_app`
#### 二版
    `celery==4.3.0`
    `redis==3.2.0`
    `kombu==4.6.11`

############ 定时任务的使用
```在tasks.py中我们定义了任务add，我已经在config.py中将该义为定时任务，现在可以启动测试```

- 启动启动定时任务首先需要启动一个调度器
    `celery beat -A celery_app.main -l info`

- 然后在重新开一个命令窗口, 开启worker执行任务
    `celery -A celery_app.main worker -l info -P eventlet`

- 在实际应用我们需要celery在后台运行，celery提供了以linux守护进程的方式，启动方式：
    `celery multi start -A celery_app.main worker -l info -P eventlet --logfile=celery.log`


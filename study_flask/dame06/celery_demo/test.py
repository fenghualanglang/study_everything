#!/usr/bin/python3.6
#具体客户端程序



from email_tasks.tasks import send_email


# 发送邮件
r1 = send_email.delay("zhangsan", "1316864657@qq.com")
print(r1.result)

















'''
celery 多work多队列

celery worker -A tasks  -l info -n workerA.%h -Q for_add_task -P eventlet
celery worker -A tasks  -l info -n workerA.%h -Q for_mix_add_task -P eventlet
celery worker -A tasks  -l info -n workerA.%h -Q for_multip_task -P eventlet
celery worker -A tasks  -l info -n workerA.%h -Q celery_task -P eventlet
'''

'''
Celery启动定时任务

- 启动启动定时任务首先需要启动一个调度器
    celery beat -A tasks -l info

- 然后在重新开一个命令窗口, 开启worker执行任务
    执行指定队列
    worker -A tasks  -l info -n workerA.%h -Q for_add_task -P eventlet
    celery -A tasks worker -l info -P eventlet


此命令在windos 无法运行
celery -A tasks worker -l info -n workerA.%h -Q for_add_task -B
'''









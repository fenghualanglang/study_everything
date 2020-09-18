#!/usr/bin/python3.6
#具体客户端程序

from celery_dm.tasks import *

# r1 = add_task.delay(120, 20)
# print ('add_task--->', r1.result)
#
# r1 = add_task.apply_async((10, 30))
# print('add_task--->', r1.result)

r2 = mix_add_task.delay(1, 2, 3)
print ('mix_add_task--->', r2.result)

    # r3 = multip_task.delay(5, 10)
    # print ('multip_task--->', r3.status)



#     # 手动执行任务
# manual_task =  manual_task.delay(333, 555)
# print('manual_task--->', manual_task.result)
# # 半自动执行任务
# semi_auto_task = semi_auto_task.delay('18236766280')
# print('semi_auto_task--->', semi_auto_task.result)
#
# # 自动执行任务
# auto_task = auto_task.delay('1316864657@qq.com')
# print('auto_task', auto_task.result)
#
# # 定时任务
# scheduler = scheduler.delay('北京今天多云转晴')
# print('scheduler--->', scheduler.result)
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









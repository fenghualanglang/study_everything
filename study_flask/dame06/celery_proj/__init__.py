# -*- coding:utf-8 -*
from celery.utils.log import get_task_logger
from celery import Task

logger = get_task_logger(__name__)

class TaskStatus(Task):

    def on_success(self, retval, task_id, args, kwargs):   # 任务成功执行
        logger.info('task id:{} , arg:{} , successful !'.format(task_id,args))

    def on_failure(self, exc, task_id, args, kwargs, einfo):  #任务失败执行
        logger.info('task id:{} , arg:{} , failed ! erros : {}' .format(task_id,args,exc))

    def on_retry(self, exc, task_id, args, kwargs, einfo):    #任务重试执行
        logger.info('task id:{} , arg:{} , retry !  einfo: {}'.format(task_id, args, exc))

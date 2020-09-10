import time

from celery_app.main import app, log


@app.task
def add(x, y):
    time.sleep(2)
    return x + y


@app.task(bind=True)  # 绑定任务
def multi(self, x, y):
    log.info(self.request.__dict__)  #打印日志
    try:
        a=[]
        a[10]==1
    except Exception as e:
        raise self.retry(exc=e, countdown=5, max_retries=3) # 出错每5秒尝试一次，总共尝试3次
    return x*y
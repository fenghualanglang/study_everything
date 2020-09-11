from celery_proj.main import app, log
from celery_proj import TaskStatus


@app.task(base=TaskStatus, bind=True)
def add(self,x,y):
    try:
        a=[]
        a[10]==1
    except Exception as e:
        raise self.retry(exc=e, countdown=5, max_retries=1) # 出错每5秒尝试一次，总共尝试1次
    return x+y

@app.task(base=TaskStatus)
def sum(a,b):
    return 'a+b={} '.format(a+b)




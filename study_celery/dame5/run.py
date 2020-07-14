#执行任务
from tasks import add
result = add.delay(4, 4)
result.ready()
result.get(timeout=1)
result.status
result.id

from celery_tasks.email_task.tasks import send_email
from celery_tasks.sms_task.tasks import send_sms
re1 = send_email.delay('zhangjunbo', '13158545657@qq.com')
print(re1.result)
re2 = send_sms.delay('zhangjunbo', '18236766280')
print(re2.result)

print(re1.status)























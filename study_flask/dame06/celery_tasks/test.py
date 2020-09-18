from celery_tasks.email_tasks.tasks import send_email
from celery_tasks.sms_tasks.tasks import send_sms


for i in range(10000):
    r = send_email.delay("zhangsan", "1316864657@qq.com")
    print(r)
    r = send_sms.delay("zhangsan", "18236766280")
    print(r)



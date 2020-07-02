

from celery_task import send_email, send_msg


result = send_email.delay('yuan')
print(result.id)

result2 = send_msg.delay('zhangsan')
print(result2.id)


# 8d511adc-f3fc-4560-9e46-885874fae955
# 275d537a-dd15-4977-b104-af77e5d55301
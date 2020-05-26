








'''
发送端
'''

import time
import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.0.110', credentials=credentials)
)

# 建立rabbit协议链接的通道
channel = connection.channel()

# 声明queue   durable=True 持久化
channel.queue_declare(queue='task_queue')

import sys

#  把脚本收到的参数合并起来，把它当做一条消息
message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()

# 发送消息内容  消息持久化
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent（就是消息持久化
    )
)

print(f'[x] sent {message}')

connection.close()





# 首先队列持久化一旦持久化，暂时不能修改， 然后消息持久化
# https://www.cnblogs.com/emptygirl/p/11411083.html












































































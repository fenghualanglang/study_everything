
# https://zhuanlan.zhihu.com/p/126702165







'''
发送端
'''


import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.56.1', credentials=credentials)
)

# 建立rabbit协议链接的通道
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')

# 发送消息内容
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='hello world'
)

print('[x] sent hello world')

connection.close()



















































































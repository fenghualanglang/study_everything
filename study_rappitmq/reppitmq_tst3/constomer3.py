



# 消息订阅发布

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

channel.exchange_declare(exchange='logs', exchange_type='fanout')#指定发送类型

#必须能过queue来收消息
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)  #随机生成的Q，绑定到exchange上面。

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue_name, callback, True)
channel.start_consuming()


# https://zhuanlan.zhihu.com/p/126702165




















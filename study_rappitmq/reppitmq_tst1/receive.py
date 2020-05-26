'''接收端'''

import pika
# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.56.1',     credentials=credentials)
)

# 建立rabbit协议链接的通道
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')


def callback(ch, method,properties, body):
    print(f'[x] receive---->{ch}, {method} {properties} {body}')

# 消费消息内容(队列， 调用函数， 是否确认)
channel.basic_consume('hello', callback, True)

print('[x] waiting formessages to exit press CTRL + C')
channel.start_consuming()



'''
ch信息
    <BlockingChannel 
        impl=<
            Channel number=1 OPEN 
            conn=<SelectConnection OPEN 
            transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x039830B0> 
            params=<ConnectionParameters host=192.168.0.110 port=5672 virtual_host=/ ssl=False>>>>

method 信息
    <Basic.Deliver(
        [
        'consumer_tag=ctag1.dfcf68bbd33b4959a734e0fe755ff4d5', 
        'delivery_tag=2', 
        'exchange=', 
        'redelivered=False', 
        'routing_key=hello'
        ]
        )>,

properties属性
    <BasicProperties> 
body 内容
    b'hello world'
'''



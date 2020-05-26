

'''
1. 发布订阅模式(路由模式 Routing)
    如果打开广播就能收到， 不打开就收不到， 错过就错过啦
    不想之如果不在线存着， 现在
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

# Exchange的作用就是转发消息，给订阅者发消息
channel.exchange_declare(exchange='logs_direct', exchange_type='direct')
#发送消息类型为fanout,就是给所有人发消息

import sys

# 严重程度
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
# 如果等于空，就输出hello world！
message = ' '.join(sys.argv[2:]) or "Hello World! %s" % time.time()

# 发送消息内容  消息持久化
channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message
)

print(f'[x] sent {message}')

connection.close()



'''
Exchange的作用就是转发消息，给订阅者发消息。

Exchange在定义的时候是有类型的，以决定到底是哪些Queue符合条件，可以接收消息。（一共有四种类型）

1、fanout: 广播  所有bind到此exchange的queue都可以接收消息 （给所有人发消息）
2、direct: 组播  通过routingKey和exchange决定的那个唯一的queue可以接收消息 （给指定的一些queue发消息）
3、topic（话题）:所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息 （给订阅话题的人发消息）
4、headers: 通过headers 来决定把消息发给哪些queue  （通过消息头，决定发送给哪些队列）

生产者将消息发送给 broker，
由交换机根据 routing_key 分发到不同的消息队列，
然后消费者同样根据 routing_key 来消费对应队列上的消息。
'''










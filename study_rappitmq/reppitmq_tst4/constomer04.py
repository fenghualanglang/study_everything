# 消息订阅发布
import sys
import time
import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')


# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.0.110', credentials=credentials)
)

channel = connection.channel()
# 建立rabbit协议链接的通道
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

# https://zhuanlan.zhihu.com/p/126702165




'''
运行方式
终端输入  python constomer04.py info

只收入info的值
'''







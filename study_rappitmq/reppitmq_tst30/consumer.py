import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.1', credentials=credentials)
)

channel = connection.channel()
# channel.queue_declare(queue='queue3', durable=True)  # 持久化
channel.queue_declare(queue='queue6', durable=True)

def callback(ch, method, properties, body):
    import time
    time.sleep(1)
    print(' [X] Receive %r' % body)
    # 消费者消费完成后返回表示符
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=10)   # 客户端一次性发给多少条给消费者， 这样保证不丢失
channel.basic_consume('queue6', callback, False)  # 默认属确认的
channel.start_consuming()

if __name__ == '__main__':
    pass





















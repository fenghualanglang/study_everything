




import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.1', credentials=credentials)
)

channel = connection.channel()
# channel.queue_declare(queue='queue3', durable=True)  # 持久化
channel.queue_declare(queue='queue5', durable=True, auto_delete=True)

def callback(ch, method, properties, body):
    print(' [X] Receive %r' % body)
    print(' [X] Done')

# 消费者
channel.basic_consume('queue5', callback, True)  # 默认属确认的
channel.start_consuming()

if __name__ == '__main__':
    pass





















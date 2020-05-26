

'''
no_ack
'''


import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.1', credentials=credentials)
)

channel = connection.channel()

# channel.queue_declare(queue='queue2')
channel.queue_declare(queue='queue6', durable=True)

for i in range(1000):
    message = 'data%d' % i
    #  发布消息
    channel.basic_publish(
        exchange='',
        routing_key='queue6',
        body=message
    )
    print('[X] sent %r ' % message)
connection.close()

if __name__ == '__main__':
    pass




'''
pika中的生产者与消费者
queue常用属性
    durable：表示持久化队列，rabbitmq服务重启后队列不丢失
    exclusive：表示队列是否对当前连接特有，其它连接不能使用，当前连接断开后队列会消失。exclusive和durable是互斥的
    auto_delete：表示当消费者不再使用队列使用时会自动删除
                不用时自动删除


'''












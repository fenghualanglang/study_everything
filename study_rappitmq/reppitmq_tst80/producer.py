

'''首部交换机'''

import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.1', credentials=credentials)
)

channel = connection.channel()

# 声明一个交换机
channel.exchange_declare(exchange='headers_ex', exchange_type='headers')

headers = {
    'key1': 'value1',
    'key2': 'value2'
}

for i in range(1000):
    message = 'data%d： %r' % (i, 'debug')
    #  发布消息
    channel.basic_publish(
        exchange='headers_ex',  # 绑定交换机
        routing_key='',        # 不需要routing_key
        body=message,
        properties=pika.BasicProperties(headers=headers)
    )
    print('[X] sent info %r ' % message)
connection.close()

if __name__ == '__main__':
    pass




'''
Exchange常用属性(durable、auto_delete)及其类型
直连交换机：direct转发消息到RK指定的队列(BK严格匹配RK)
    # 直连交换机广播，接收到能收到就收到，类似于udp
    # 如果是持久队列， 消费者能就收到

扇形交换机：fanout 转发消息到所有绑定队列
    # 不是基于routing_key与binding_key 消息的转发的
    # 将消息转发给所有绑定的消息队列， 如果一个交换机绑定多条消息队列， 那么这条消息队列都会收到这条消息队列，类似于广播

主题交换机：topic按RK规则转发(BK模糊匹配RK)
首部交换机：headers根据发送消息中的headers属性进行匹配 
'''












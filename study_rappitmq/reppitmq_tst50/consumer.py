

import pika

# 输入普通凭据(登录用户名和密码)
credentials = pika.PlainCredentials('zhangsan', '1qaz2wsx')

# 输入连接参数(阻塞连接)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.56.1', credentials=credentials)
)

channel = connection.channel()

# 声明一个交换机
channel.exchange_declare(exchange='direct_ex', exchange_type='direct')


# 这里如果不写queue参数，那么意味着服务器随机产生一个队列
# 由于还加上exclusive, 所以这就是实现了临时队列， 链接已关闭，该队列也会删除
# queue='', exclusive=True 随机生成队列只在当前链接使用， 关闭默认删除

# result = channel.queue_declare(queue='', exclusive=True)
# # 每个消费之有自己的消费队列
# queue_name = result.method.queue

queue_name = 'new_queue'
channel.queue_declare(queue=queue_name)

# 指当前队列要接受routing_key指为debug、info、warning的消息
binding_keys = ['debug', 'info', 'warning']

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='direct_ex',  # 绑定交换机
        queue=queue_name,
        routing_key=binding_key
    )

print('[X] waiting for logs. to exit press ctrl + c ')
def callback(ch, method, properties, body):
    print(f"[X] {method.routing_key}, {body.decode('utf-8')}")

channel.basic_consume(queue_name, callback, True)  # 默认属确认的
channel.start_consuming()

if __name__ == '__main__':
    pass




'''
Exchange常用属性(durable、auto_delete)及其类型
直连交换机：direct转发消息到RK指定的队列(BK严格匹配RK) 
扇形交换机：fanout 转发消息到所有绑定队列
主题交换机：topic按RK规则转发(BK模糊匹配RK)
首部交换机：headers根据发送消息中的headers属性进行匹配 
'''








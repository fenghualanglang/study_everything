
'''
一个生产者多个消费者，rabbiMQ会默认吧product发出的消息依次分发给各个消费者，跟负载均衡差不多

1. 加入任务处理一般死了？怎么办？
    消息被消费者拿走并没有删除，必须把任务处理完成后给服务器一个响应，这时才被真正消灭了
    如果消费者没有回馈，消息继续放回到队列中

    delivery_tag 消费端消费完成随机生成一个标记





此时，先启动消息生产者，然后再分别启动3个消费者，通过生产者多发送几条消息，你会发现，这几条消息会被依次分配到各个消费者身上执行任务可能需要几秒钟。
您可能想知道，如果其中一个使用者开始一项漫长的任务并仅部分完成而死掉，会发生什么情况。使用我们当前的代码，RabbitMQ一旦将消息传递给客户，便立即将其从内存中删除。
在这种情况下，如果您杀死一个工人，我们将丢失正在处理的消息。我们还将丢失所有发送给该特定工作人员但尚未处理的消息。

但是我们不想丢失任何任务。如果一个工人死亡，我们希望将任务交付给另一个工人。
为了确保消息永不丢失，RabbitMQ支持消息  确认。使用者发送回一个确认（acknowledgement），以告知RabbitMQ已经接收，处理了特定的消息，并且RabbitMQ可以自由删除它。

如果使用者在不发送确认的情况下死亡（其通道已关闭，连接已关闭或TCP连接丢失），RabbitMQ将了解消息未完全处理，并将重新排队。
如果同时有其他消费者在线，它将很快将其重新分发给另一位消费者。这样，即使工人偶尔死亡，您也可以确保不会丢失任何消息。

没有任何消息超时；消费者死亡时，RabbitMQ将重新传递消息。即使处理一条消息花费非常非常长的时间也没关系。

消息确认默认情况下处于打开状态。在前面的示例中，我们通过no_ack = True标志显式关闭了它们  。我们完成任务后，是时候删除此标志并从工作人员发送适当的确认了。






'''


# 消费者代码
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

# 声明queue    durable=True持久化
channel.queue_declare(queue='task_queue')


def callback(ch, method,properties, body):
    print(f'[x]receive msg .... start processing ...{body}')
    time.sleep(20)
    print("[x] Done")
    print("method.delivery_tag",method.delivery_tag)

    # 消费者消费完成后返回表示符
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 消费消息内容(队列， 调用函数， 是否确认)
channel.basic_consume('task_queue', callback)  # 默认属确认的

print('[x] waiting formessages to exit press CTRL + C')
channel.start_consuming()




# （一个发消息，两个收消息，收消息是公平的依次分发
































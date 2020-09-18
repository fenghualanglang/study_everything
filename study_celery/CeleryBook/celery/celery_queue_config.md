# celery 的多任务 多队列

celery是一个分布式的任务调度模块，那么怎么实现它的分布式功能呢，celery可以支持多台不同的计算机执行不同的任务或者相同的任务。

如果要说celery的分布式应用的话，就要提到celery的消息路由机制，提到AMQP协议。

简单理解：

可以有多个"消息队列"（message Queue），不同的消息可以指定发送给不同的Message Queue，

而这是通过Exchange来实现的，发送消息到"消息队列"中时，可以指定routiing_key，Exchange通过routing_key来吧消息路由（routes）到不同的"消息队列"中去。

 exchange 对应 一个消息队列(queue)，即：通过"消息路由"的机制使exchange对应queue，每个queue对应每个worker。 

![celery-queue-structure](images/celery-queue-structure.png)
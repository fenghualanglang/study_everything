



# asyncio 提供的的是事件循环为中心的，负责高效的处理I/O事件

# event_loop:时间循环，开启之后，可以将协程注册进来。
# task：一个协程对象就是一个可以挂起的函数，任务是对协程的进一步封装，其中包含了任务的各种状态
# future: 期物，代表将来执行或没有执行的任务的结果。task可以说是future的子类。


import asyncio
import time

async def get_html(url):

    print('start get url')

    await asyncio.sleep(2)
    print('end get url')


if __name__ == '__main__':
    url = 'www.baidu.com'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_html(url))

    # tasks 里面放的是协成对象
    tasks = [get_html(url) for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('等到10次运行完成后才会执行这一步')


# asyncio 启动 把协成传入这个方法run_until_complete()
# asyncio.wait() 可执行一个可迭代对象，执行完成后才会执行后一步
# await asyncio.sleep(2)  并发模式等待，会发现其几乎同时执行完成
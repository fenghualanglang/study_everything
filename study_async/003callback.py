'''
协成的返回值
协成执行完成后调用其他常规函数
    1.无参数
    2.有参数
'''

import asyncio
import functools


async def get_html(url):
    print('start_url')
    await asyncio.sleep(3)
    return 'laowang'

def callback(future):
    print('send email to bobby')

def callback2(url, future):  # 协成执行后执行此函数， 参数前， 协成后
    print(url)

if __name__ == '__main__':
    url = 'www.baidu.com'
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html(get_html(url)))
    task.add_done_callback(callback)
    loop.run_until_complete(task)
    print(task.result())    #

    # 获取协成的返回值， 如何进行有参数的执行
    wrapped = functools.partial(callback2, url)
    task.add_done_callback(wrapped)

    loop.run_until_complete(task)
    print(task.result())

# add_done_callback() 上面函数执行后，执行此函数 无参数传入函数，有参数利用functools
# functools.partial(函数, 参数)










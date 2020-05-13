
'''
asyncio.wait(tasks) 一次性提交多个任务时派上用上了，会等到此步完成后才能执行下一步
asyncio.gather(*tasks)
'''

import asyncio

async def get_html(url):

    print(f'start get url  {url}')

    await asyncio.sleep(2)
    print('end get url')


if __name__ == '__main__':
    url = 'www.baidu.com'
    loop = asyncio.get_event_loop()
    tasks = [get_html(url) for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # loop.run_until_complete(asyncio.gather(*tasks))
    # *tasks 将其解析为参数

    url2 = 'www.taobao.com'
    group1 = [get_html(url) for i in range(10)]
    group2 = [get_html(url2) for i in range(10)]

    # asyncio.gather() 可将协成对象分开传递 *
    loop.run_until_complete(asyncio.gather(*group1, *group2))
    # asyncio.gather() 另一种传递方法
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    loop.run_until_complete(asyncio.gather(group1, group2))

    # asyncio.gather() 也可以取消任务
    group2.cancel()





































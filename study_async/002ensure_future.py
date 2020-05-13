# future获取返回值

import asyncio

async def get_html(url):
    print('sta')
    return '234'

if __name__ == '__main__':
    url = 'www.baidu.com'
    loop = asyncio.get_event_loop()

    get_future = asyncio.ensure_future(get_html(url))
    loop.run_until_complete(get_future)
    print(get_future.result())

    task = loop.create_task(get_html(url))
    loop.run_until_complete(task)
    print(task.result())

# run_until_complete  可接受协成类型，可接受ensure_future类型
# ensure_future 与 create_task  接受的是协成类型， task是future的子类
# get_future.result() 或 task.result()， 返回的结果是return的结果



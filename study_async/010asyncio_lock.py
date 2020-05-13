


import asyncio

total = 0

# async def add():
#
#     global total
#     for i in range(10000):
#         total += 1
#
# async def desc():
#     global total
#     for i in range(10000):
#         total -= 1
#
# if __name__ == '__main__':
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(total)

# import aiohttp
# import asyncio
# from asyncio import Lock, Queue
# cache = {}
# lock = Lock()
# queue = Queue  #此处的queue可进行限流
#
# # await queue.get()
#
# async def get_stuff(url):  # 获取一段url
#
#     async with await lock:
#         if url in cache:
#             return cache[url]
#         stuff = aiohttp.request("GET", url)
#         cache[url] = stuff
#         return stuff
#
#
# async def parse_stuff():
#
#    stuff = await get_stuff()
#    # do some parsing
#
# async def use_stuff():
#     stuff = await get_stuff()
#     # use stuff to do something interesting
#
# if __name__ == '__main__':
#     tasks = [parse_stuff(), use_stuff()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))



import asyncio
from asyncio import Lock
import functools

def unlock(lock):
    print('callback releasing lock')


async def coro1(lock):
    print('coro1 waiting for the lock')
    with await lock:
        print('coro1 acquired lock')
    print('coro1 released lock')

async def coro2(lock):
    print('coro2 waiting for the lock')
    await lock

    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


async def main(loop):
    # create and acquire a shared lock
    lock = Lock()
    print('acquiring the lock before starting coroutiones')
    await lock.acquire()
    print(f'lock acquired {lock.locked()}')

    # schedule a callback to unlock the lock
    loop.call_later(1, functools.partial(unlock, loop))

    # run the coroutiones that want to use the lock
    print('waiting for coroutiones')
    await asyncio.wait([coro1(lock), coro2(lock)])


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main(loop))
finally:
    loop.close()



















































































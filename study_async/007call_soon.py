



'''
call_soon 等待下次循环式即刻执行
call_later(秒， 函数, 参数)  等待多少秒后执行
'''

import asyncio

def callback(sleep_times):

    print(f'sleep {sleep_times} sucess')

def stoploop(loop):
    loop.stop()



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # call_soon 等待下次循环式即刻执行
    loop.call_soon(callback, 2)

    # call_later(秒， 函数, 参数)  等待多少秒后执行
    loop.call_later(3, stoploop, loop)

    # loop.call_soon(stoploop, loop)
    loop.run_forever()




# import asyncio
#
# def callback(arg, args):
#
#     print(f'calllback invoked with {arg} and {args}')
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.call_soon(callback, 1, (4,))
#     loop.run_forever()
#


















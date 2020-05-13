


'''
协成的嵌套
'''



import asyncio

async def compute(x, y):

    print(f'Compute {x} + {y}')
    await asyncio.sleep(2)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)

    print(f'{x} + {y} = {result}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()



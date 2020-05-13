
'''

取消future(task)
'''

# run_forever() 运行完成后，时间循环不会停止
# run_until_complete() 运行完成后，时间循环停止

import asyncio

async def get_hml(t):

    await asyncio.sleep(t)

    print(t, '--')


if __name__ == '__main__':
    task1 = get_hml(2)
    task2 = get_hml(3)
    task3 = get_hml(3)
    tasks = [task1, task2, task3]
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasls = asyncio.Task.all_tasks()
        for task in all_tasls:
            print('cancel task')
            print(task.cancel())
        loop.stop()
        # loop.run_forever()
    finally:
        loop.close()


    # loop.run_forever()
    # loop.run_until_complete()

# asyncio.Task.all_tasks()   获取所有的任务


